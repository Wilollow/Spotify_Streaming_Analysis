import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

spotify_df = pd.read_json("spotify_history.json", convert_dates=True)

spotify_df["timestamp"] = pd.to_datetime(spotify_df["timestamp"])
spotify_df = spotify_df.sort_values("timestamp")

hourly_distribution = spotify_df.groupby(spotify_df["timestamp"].dt.hour)["listening_duration_seconds"].sum()
daily_distribution = spotify_df.groupby(spotify_df["timestamp"].dt.day_of_week)["listening_duration_seconds"].sum()

hourly_angles = np.arange(len(hourly_distribution.index)) * 2 * np.pi / len(hourly_distribution.index)
daily_angles = np.arange(len(daily_distribution.index)) * 2 * np.pi / len(daily_distribution.index)


fig, ax = plt.subplots(1,2,subplot_kw=dict(polar=True),figsize=(18, 10))
bars = ax[0].bar(hourly_angles, hourly_distribution.values)

ax[0].set_title(f"Hourly listening distribution")
ax[0].set_xticks(hourly_angles)
ax[0].set_xticklabels([f"{hour : 03d}:00" for hour in hourly_distribution.index])
ax[0].set_yticks([0])

bars = ax[1].bar(daily_angles, daily_distribution.values)

ax[1].set_title(f"Daily listening distribution")
ax[1].set_xticks(daily_angles)
ax[1].set_xticklabels([f"{["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][day]}" for day in daily_distribution.index])
ax[1].set_yticks([0])

plt.tight_layout()
plt.savefig(f"./results/hourly_weekly_distribution.png", dpi=150)
print(f"Result saved in results/hourly_weekly_distribution.png")
# plt.show()