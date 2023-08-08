"""
Reads in the text file which contains the scrapted dictonary 
of the Top 100 songs each week since 1958 and converts it into a dataframe, 
which is saved as a csv 
"""


import pandas as pd 
import ast
import os 

CURRENT_DIR = os.path.dirname(__file__)


with open(os.path.join(CURRENT_DIR,'Data/topArtists.txt')) as file: 
    
    lines = file.readlines()

    data = {'date' : [], 'rank' : [], 'artist' : [], 'song' : []}
    
    big_data =   pd.DataFrame.from_dict(data, orient='index').transpose()
    
    for i in range(len(lines)):

        if i < len(lines)-1:
            date = lines[i][1:11]
            values = lines[i][14:len(lines[i])-2]
        else: 
            date = lines[i][1:11]
            values = lines[i][14:len(lines[i])] 
            
        
        
    
        values_dict = ast.literal_eval(values)
        
        list_values = list(values_dict.values())
        
        keys = values_dict.keys()
        
        year = date[0:4]  
        month = date[5:7]
        
        
        dates = []
        years = []
        months = []
        ranks = []
        songs = []
        artists = []
        
    
        for i in range(len(list_values)): 
            
            item = str(list_values[i])
            
            art, son = item.split(", '")
            
            art = art[12:len(art)-1]
            son = son[8:len(son)-2]
            
            
            years.append(year)
            months.append(month)
            dates.append(date)
            ranks.append(i+1)
            artists.append(art)
            songs.append(son)
            
            
            
        data = {'year' : years,'month': months, 'date' : dates, 'rank' : ranks, 'artist' : artists, 'song' : songs}
        
        dataframe = pd.DataFrame.from_dict(data, orient='index').transpose()
        
        big_data = pd.concat([big_data, dataframe])
        
        
        big_data.to_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_artists_weekly_as_Dataframe.csv'))
        

    
        
        
        
        
        
        
        
    
   
   
        
    
    