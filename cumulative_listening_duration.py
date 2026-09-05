import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

spotify_df = pd.read_json("spotify_history.json", convert_dates=True)

args = sys.argv

TOP_X = int(args[1])

spotify_df["timestamp"] = pd.to_datetime(spotify_df["timestamp"])
spotify_df = spotify_df.sort_values("timestamp")
top_artists = spotify_df.groupby("album_artist")["listening_duration_seconds"].sum().sort_values(ascending=False).head(TOP_X).index.tolist()

df_top = spotify_df[spotify_df["album_artist"].isin(top_artists)].copy()

df_top["listen_time_hours"] = df_top["listening_duration_seconds"]/3600

pivot = (
    df_top.pivot_table(index="timestamp", columns="album_artist", values="listen_time_hours", aggfunc="sum")
    .fillna(0)
    .reindex(columns=top_artists)  # keep columns ordered by rank
)
cumulative = pivot.cumsum()

fig, ax = plt.subplots(figsize=(18, 10))
for artist in top_artists:
    ax.plot(cumulative.index, cumulative[artist], label=artist, linewidth=1.8)
 
ax.set_title(f"Cumulative listening duration Over Time — Top {TOP_X} Artists")
ax.set_xlabel("Date")
ax.set_ylabel("Hours listened")
ax.legend(loc="upper left", fontsize=9, ncol=2)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax.grid(alpha=0.3)
fig.autofmt_xdate()
 
plt.tight_layout()
plt.savefig(f"./results/cumulative_duration_top_{TOP_X}_artists.png", dpi=150)
print(f"Result saved in results/cumulative_duration_top_{TOP_X}_artists.png")
# plt.show()