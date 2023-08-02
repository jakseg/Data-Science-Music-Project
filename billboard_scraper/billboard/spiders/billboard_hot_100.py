import datetime
import scrapy
import json


class BillboardHot100(scrapy.Spider):
    name = "billboard"

    def start_requests(self):
        weeks = self.iterate_weeks(2000, 8, 4)
        for week in weeks:
            url = f"https://www.billboard.com/charts/hot-100/{week}"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        year = response.url.split("/")[-2]  # Extract the year from the URL
        week = response.url.split("/")[-1]

        top_songs = response.css(".chart-results-list .c-title.a-no-trucate ::text").getall()
        top_songs = [song.strip() for song in top_songs]
        top_artists = response.css(".chart-results-list .c-label.a-no-trucate ::text").getall()
        top_artists = [artist.strip() for artist in top_artists]

        artist_song_dict = {}
        for index, artist in enumerate(top_artists):
            artist_song_dict[index + 1] = {
                "artist": artist,
                "song": top_songs[index]
            }

        self.append_to_dictionary(artist_song_dict, f"topArtists.txt", year, week)
        yield None

    def append_to_dictionary(self, dictionary, filename, year, week):
        with open(filename, 'a') as file:
            if file.tell() != 0:
                file.write(",\n")
            file.write(f'"{year}_{week}": {json.dumps(dictionary)}')

    def write_dictionary_to_file(self, dictionary, filename):
        with open(filename, 'x') as file:  # Use 'x' mode to create the file
            file.write(json.dumps(dictionary))

    def iterate_weeks(self,start_year, start_month, start_day):
        current_date = datetime.date(start_year, start_month, start_day)
        end_date = datetime.date.today()

        one_week = datetime.timedelta(days=7)
        weeks = []
        while current_date <= end_date:
            weeks.append(current_date.strftime("%Y-%m-%d"))
            print(current_date.strftime("%Y-%m-%d"))
            current_date += one_week
        return weeks


