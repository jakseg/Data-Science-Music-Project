"""
Extracts new dataframe with only the top 10 songs of each year from dataframe with top 100 songs. 
Creates a scatter plot for top 100 and top 10 songs and computes a regression of order 2 for each. 
Creates plot which compares regressions of top 100 and top 10 with each other. 
"""

import numpy 
import pandas as pd 
import matplotlib.pyplot as plt
import os

CURRENT_DIR = os.path.dirname(__file__)  # Gets directory path of the current python module

data = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_artists_songs_per_year_with_duration.csv'))


data_short = data.groupby(['year'], group_keys = False)
data_short = data_short.apply(lambda x: x.sort_values('points').head(10)).reset_index()

data_short = data_short.groupby(['year'])['duration'].mean().reset_index()

X_short = data_short['year'].values.reshape(-1, 1)
Y_short = data_short['duration'].values.reshape(-1, 1)

model = numpy.poly1d(numpy.polyfit(data_short['year'],data_short['duration'],2))
Y_short_pred = model(X_short)

plt.figure()
plt.scatter(X_short,Y_short, color = 'teal')
plt.plot(X_short, Y_short_pred, color = 'darkslategray')
plt.title("Mean of the duration of the Top 10 songs per year with regression")
plt.xlabel('Year')
plt.ylabel('Duration in secs')

# Save plot
plt.savefig(f"{CURRENT_DIR}/Plots/Mean_Duration_Top_10_Songs_Per_Year_With_Regression.svg")

data = data.groupby(['year'])['duration'].mean().reset_index()

X = data['year'].values.reshape(-1, 1)
Y = data['duration'].values.reshape(-1, 1)

model = numpy.poly1d(numpy.polyfit(data['year'],data['duration'],2))
Y_pred = model(X)

plt.figure()
plt.scatter(X,Y, color = 'navy')
plt.plot(X, Y_pred, color = 'royalblue')
plt.title("Mean of the duration of the Top 100 songs per year with regression")
plt.xlabel('Year')
plt.ylabel('Duration in secs')

# Save plot
plt.savefig(f"{CURRENT_DIR}/Plots/Mean_Duration_Top_100_Songs_Per_Year_With_Regression.svg")



plt.figure(figsize=(12, 6))
plt.title(label = 'Comparison of the mean duration of Top 100 and Top 10 songs per year')
plt.plot(X_short, Y_short_pred, color = 'teal', label = 'Top 10')
plt.plot(X, Y_pred, color = 'navy', label = 'Top 100')
plt.xlabel('Year')
plt.ylabel('Duration in secs')
plt.legend(bbox_to_anchor=(1.04, 0.5), loc ="center left", borderaxespad = 0)

# Save plot
plt.savefig(f"{CURRENT_DIR}/Plots/Comparison_Top_10_and_Top_100_Regression.png")


