import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

spotify_df = pd.read_json("spotify_history.json", convert_dates=True)

args = sys.argv

# X_DAYS = int(args[1])
PERIOD = f"W" # "D" = daily, "W" = weekly, "ME" = monthly


spotify_df["timestamp"] = pd.to_datetime(spotify_df["timestamp"])
spotify_df = spotify_df.sort_values("timestamp")
spotify_df["play"] = 1

# total_per_period = spotify_df.resample(PERIOD).count()

# resampler = spotify_df.resample(PERIOD) 

# print(spotify_df.groupby('album_artist').agg({"listening_duration_seconds":sum}))
# print(spotify_df.agg({"listening_duration_seconds":"sum"}))

weekly_artist_time = (
    spotify_df.groupby([pd.Grouper(key="timestamp", freq=PERIOD), "album_artist"])
      ["listening_duration_seconds"]
      .sum()
)

weekly_p_artist = weekly_artist_time / (weekly_artist_time.groupby(level=0).transform("sum"))
weekly_entropy_artist = (-weekly_p_artist * np.log(weekly_p_artist)).fillna(0).groupby("timestamp").sum()
weekly_artist_count = weekly_artist_time.groupby(level=0).size()
corrected_weekly_entropy_artist = (weekly_entropy_artist / np.log(weekly_artist_count)).fillna(0)

weekly_album_time = (
    spotify_df.groupby([pd.Grouper(key="timestamp", freq=PERIOD), "album_name"])
      ["listening_duration_seconds"]
      .sum()
)

weekly_p_album = weekly_album_time / (weekly_album_time.groupby(level=0).transform("sum"))
weekly_entropy_album = (-weekly_p_album * np.log(weekly_p_album)).fillna(0).groupby("timestamp").sum()
weekly_album_count = weekly_album_time.groupby(level=0).size()
corrected_weekly_entropy_album = (weekly_entropy_album / np.log(weekly_album_count)).fillna(0)



fig, ax = plt.subplots(figsize=(18, 10))
ax.plot(corrected_weekly_entropy_artist.index, corrected_weekly_entropy_artist, label="artist entropy", linewidth=1.8)
ax.plot(corrected_weekly_entropy_album.index, corrected_weekly_entropy_album, label="album entropy", linewidth=1.8)
# ax.plot(weekly_artist_count.index,weekly_artist_count/weekly_artist_count.max(),label=f"weekly artist count. normalised", linewidth=1.8)

ax.set_title(f"Listening Entropy over time")
ax.set_xlabel("Date")
ax.set_ylabel("Corrected entropy")
ax.legend(loc="upper left", fontsize=9, ncol=2)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax.grid(alpha=0.3)
fig.autofmt_xdate()
 
plt.tight_layout()
plt.savefig(f"./results/entropy.png", dpi=150)
print(f"Result saved in results/entropy.png")
# plt.show()