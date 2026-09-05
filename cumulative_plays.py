import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

spotify_df = pd.read_json("spotify_history.json", convert_dates=True)

args = sys.argv

TOP_X = int(args[1])
MIN_DURATION = int(args[2])


spotify_df["timestamp"] = pd.to_datetime(spotify_df["timestamp"])
spotify_df = spotify_df[spotify_df["listening_duration_seconds"] >= MIN_DURATION].copy()
spotify_df = spotify_df.sort_values("timestamp")

top_artists = spotify_df["album_artist"].value_counts().head(TOP_X).index.tolist()

df_top = spotify_df[spotify_df["album_artist"].isin(top_artists)].copy()
df_top["play"] = 1

pivot = (
    df_top.pivot_table(index="timestamp", columns="album_artist", values="play", aggfunc="sum")
    .fillna(0)
    .reindex(columns=top_artists)  # keep columns ordered by rank
)

cumulative = pivot.cumsum()

fig, ax = plt.subplots(figsize=(18, 10))
for artist in top_artists:
    ax.plot(cumulative.index, cumulative[artist], label=artist, linewidth=1.8)
 
ax.set_title(f"Cumulative Plays Over Time — Top {TOP_X} Artists")
ax.set_xlabel("Date")
ax.set_ylabel("Cumulative Play Count")
ax.legend(loc="upper left", fontsize=9, ncol=2)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax.grid(alpha=0.3)
fig.autofmt_xdate()
 
plt.tight_layout()
plt.savefig(f"./results/cumulative_plays_top_{TOP_X}_artists.png", dpi=150)
print(f"Result saved in results/cumulative_plays_top_{TOP_X}_artists.png")
# plt.show()