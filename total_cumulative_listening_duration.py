import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

spotify_df = pd.read_json("spotify_history.json", convert_dates=True)

spotify_df["timestamp"] = pd.to_datetime(spotify_df["timestamp"])
spotify_df = spotify_df.sort_values("timestamp")

spotify_df["listen_time_hours"] = spotify_df["listening_duration_seconds"]/3600

pivot = (
    spotify_df.pivot_table(index="timestamp", values="listen_time_hours", aggfunc="sum")
    .fillna(0)
)

cumulative = pivot.cumsum()

fig, ax = plt.subplots(figsize=(18, 10))
ax.plot(cumulative.index, cumulative["listen_time_hours"], label="total listening duration", linewidth=1.8)
 
ax.set_title(f"Cumulative listening duration Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Hours listened")
ax.legend(loc="upper left", fontsize=9, ncol=2)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax.grid(alpha=0.3)
fig.autofmt_xdate()
 
plt.tight_layout()
plt.savefig(f"./results/total_cumulative_duration.png", dpi=150)
print(f"Result saved in results/total_cumulative_duration.png")
# plt.show()