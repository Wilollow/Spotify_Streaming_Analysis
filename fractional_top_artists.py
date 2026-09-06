import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

spotify_df = pd.read_json("spotify_history.json", convert_dates=True)

args = sys.argv

TOP_X = int(args[1])
FRACTIONAL_DISPLAY = (args[2] == "1")
PERIOD = "W"

spotify_df["timestamp"] = pd.to_datetime(spotify_df["timestamp"])
spotify_df = spotify_df.sort_values("timestamp")
top_artists = spotify_df.groupby("album_artist")["listening_duration_seconds"].sum().sort_values(ascending=False).head(TOP_X).index.tolist()

# Do you want the weekly listening duration of your top artists to be graphed as a percentage of your weekly total listening duration? Enter 1 for yes, 2 for no

weekly_artist_listening_duration = (
    spotify_df[spotify_df["album_artist"].isin(top_artists)].groupby([pd.Grouper(key="timestamp", freq=PERIOD),"album_artist"])
      ["listening_duration_seconds"]
      .sum()/3600
)

weekly_listening_duration = (
    spotify_df.groupby(pd.Grouper(key="timestamp", freq=PERIOD))
      ["listening_duration_seconds"]
      .sum()/3600
)

if FRACTIONAL_DISPLAY:
    weekly_artist_listening_duration/=weekly_listening_duration / 100

fig, ax = plt.subplots(figsize=(18, 10))
for artist in top_artists:
    data = weekly_artist_listening_duration.xs(artist,level="album_artist")
    ax.plot(data.index,data.values,label=artist, linewidth=1.8)

ax.set_title(f"Weekly listening duration Over Time — Top {TOP_X} Artists")
ax.set_xlabel("Date")
ax.set_ylabel(f"{"percentage of weekly listening duration" if FRACTIONAL_DISPLAY else "Weekly listening duration (Hours)"}")
ax.legend(loc="upper left", fontsize=9, ncol=2)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax.grid(alpha=0.3)
fig.autofmt_xdate()

plt.tight_layout()
plt.savefig(f"./results/weekly_listening_duration_top_{TOP_X}_artists.png", dpi=150)
print(f"Result saved in results/weekly_listening_duration_top_{TOP_X}_artists.png")
# plt.show()