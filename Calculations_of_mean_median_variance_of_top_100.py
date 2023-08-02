"""
Creates line plot of mean and median of the top 100 for each year. 
Creates line plot of variance of the the top 100 for each year. 
"""

import os 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

CURRENT_DIR = os.path.dirname(__file__) 

data = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_artists_songs_per_year_with_duration.csv'))

data = data.groupby(['year'])['duration'].agg(['mean', 'median', 'var']).reset_index()



plt.figure()
plt.title(label = 'Mean and median of the duration of the Top 100 songs per year')
plt.ylabel('Duration in sek')
plt.xlabel('Year')
sns.lineplot(data = data, x = 'year', y = 'mean', label = 'Mean', color = 'navy')
sns.lineplot(data = data, x = 'year', y = 'median', label = 'Median', color = 'cornflowerblue')
plt.legend(bbox_to_anchor=(1.04, 0.5), loc ="center left", borderaxespad = 0)

plt.figure()
plt.title(label = "Variance of duration of the Top 100 songs per year")
plt.xlabel('Year')
plt.ylabel('Variance in secs^2')
sns.lineplot(data = data, x = 'year', y = 'var', color = 'slateblue')

# Save plot
CURRENT_DIR = os.path.dirname(__file__)
plt.savefig(f"{CURRENT_DIR}/Plots/Variance_of_Top_100_songs_per_year.svg")
