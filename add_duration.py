"""
Adds duration to each song using the Spotify API
"""

import csv
import requests
import os 

CURRENT_DIR = os.path.dirname(__file__)

#all_songs_csv = pd.read_csv(os.path.join(CURRENT_DIR, "Data/Top_100_artists_songs_per_year_with_duration.csv"))

input_file = os.path.join(CURRENT_DIR, "./Top_100_country_songs_per_year.csv")
output_file = os.path.join(CURRENT_DIR, "./Top_100_country_songs_per_year_with_duration.csv")


duration_cache = {}

def get_song_duration(song_name):
    if song_name in duration_cache:
        return duration_cache[song_name]
    
    # Spotify API - Insert valid token
    endpoint = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": "Bearer BQDYjc8rRa1OIWiPhxn2ZBwXYxjOP8-gur8SG3PIwC1N7fiixWg0z-tzQDAyJZzyE4aOOJrZeRqqe8871DqKlOu60Su_LMU_mcg07T3B8Ho9yzNjB5g"
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