"""
Creates plot with Zoom-In into mean duration of the top 100 songs for each 
month in the years between 2005 and 2023. 
Point is mean duration of one month of this year. 
Additional a regression of order two is computed. 
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CURRENT_DIR = os.path.dirname(__file__)

data = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_artists_songs_per_year_month_with_duration.csv'))
dataAll = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_artists_songs_per_year_with_duration.csv'))



data_short = data.groupby(['year', 'month'], group_keys = False)
data_short = data_short.apply(lambda x: x.sort_values('points').head(100)).reset_index()

data_short = data_short.groupby(['year', 'month'])['duration'].mean().reset_index()

dabata = data_short.groupby(['year'])['duration'].mean().reset_index()

X_short = data_short['year'].values.reshape(-1, 1)
Y_short = data_short['duration'].values.reshape(-1, 1)

model = np.poly1d(np.polyfit(data_short['year'],data_short['duration'],2))
Y_short_pred = model(X_short)

plt.figure(figsize=(12,5))
plt.xticks(np.arange(2005, 2023, step=1))
plt.scatter(X_short,Y_short, color = 'steelblue')
plt.plot(X_short, Y_short_pred, color = 'slateblue')
#plt.plot(X_short, Y_short_pred, color = 'mediumaquamarine')
plt.title("Mean of the duration of the Top 100 songs per year between 2005 and 2023 with regression of order 2")
plt.xlabel('Year')
plt.ylabel('Duration in secs')

plt.savefig(f"{CURRENT_DIR}/Plots/Mean_Duration_with_Regression_Order_2_Top_100_Monthly.svg")
