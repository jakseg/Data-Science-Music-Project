"""
Adds duration to each song using the Spotify API.
If it doesn't go through, the Bearer Token needs to be updated or Spotify doesn't know the song by that name. 
Then it must be adjusted manually in the input file.
"""

import csv
import requests
import os 

CURRENT_DIR = os.path.dirname(__file__)

#Change the directory to create new files
input_file = os.path.join(CURRENT_DIR, "Data/Top_100_R&B_songs_per_year.csv")
output_file = os.path.join(CURRENT_DIR, "Data/Top_100_R&B_songs_per_year_with_duration.csv")


duration_cache = {}

def get_song_duration(song_name):
    if song_name in duration_cache:
        return duration_cache[song_name]
    
    #Spotify API - Insert valid token
    endpoint = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": "Bearer -INSERT YOUR TOKEN HERE-"
    }
    params = {
        "q": song_name,
        "type": "track",
        "limit": 1
    }

    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        track = data["tracks"]["items"][0]
        duration_ms = track["duration_ms"]
        duration_sec = duration_ms / 1000
        
        duration_cache[song_name] = duration_sec
        
        return duration_sec
    else:
        print(f"Fehler bei der API-Anfrage für den Song '{song_name}'.")
        return None


with open(input_file, 'r') as file, open(output_file, 'w', newline='') as output:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames + ['duration']
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        song_name = row['song']
        duration = get_song_duration(song_name)

        if duration is not None:
            row['duration'] = duration
        else:
            row['duration'] = ""

        writer.writerow(row)

print("The duration of the songs was successfully added to the CSV file!")
