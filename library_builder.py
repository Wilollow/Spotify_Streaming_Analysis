import os
import json
folder = os.getcwd() + "/data"

def list_files(dir_path):
    try:
        return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    except OSError:
        return []
    
if len(list_files(folder)) == 0:
    print("no appropriate files found in data folder. Are you sure you copied all files from the correct zip file?")
    

listen_history = []

for file_name in list_files(folder):
    if "Audio" in file_name:
        with open(f"{folder}/{file_name}", "r", encoding="utf-8") as history_list:
            l = json.load(history_list)
            print(f"Loading {file_name} with {len(l)} records")
            listen_history.extend(l)
            
cleaned_history = []

print("cleaning data..")

for event in listen_history:
    cleaned_history.append({
        "timestamp": event["ts"],
        "track_title": event["master_metadata_track_name"],
        "album_artist": event["master_metadata_album_artist_name"],
        "album_name": event["master_metadata_album_album_name"],
        "listening_duration_seconds": event["ms_played"]/1000
    })

print("creating spotify_history.json...")

with open("spotify_history.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_history, f, indent=4)