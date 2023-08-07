"""
Calculates the Top 100 songs of each year and creates a new csv 
to which the duration will be added in the next step

"""
 
import pandas as pd 
import os 


CURRENT_DIR = os.path.dirname(__file__)
big_data = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_artists_weekly_as_Dataframe.csv'))


top_100_year_sum_of_ranks = big_data.groupby(['year', 'song', 'artist'])['rank'].sum().reset_index().rename(columns={'rank': 'sum_of_ranks'})

top_100_year_count_song_per_year = big_data.groupby(['year', 'song', 'artist'])['rank'].count().reset_index().rename(columns={'rank': 'count_of_weeks'})



top_100_year = top_100_year_sum_of_ranks.merge(top_100_year_count_song_per_year, on = ['year', 'song', 'artist'])


top_100_year['points'] = (52 - top_100_year['count_of_weeks']) * 101 +  top_100_year['sum_of_ranks']

top_100_year = top_100_year.groupby(['year'], group_keys = False)

top_100_year = top_100_year.apply(lambda x: x.sort_values('points').head(100)).reset_index()

top_100_year = top_100_year[['year', 'artist', 'song', 'points']]

top_100_year.to_csv( os.path.join(CURRENT_DIR,'Data/Top_100_artists_songs_per_year.csv'))

