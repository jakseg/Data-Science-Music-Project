"""
Creates a plot which shows the regressions of the mean duration of the top 100 
songs of each year for different genres. 
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def calculate_mean_each_year(dataframes):
    x_set = []
    y_set = []
    for dataframe in dataframes:
        data_short = dataframe.groupby(['year'], group_keys=False)
        data_short = data_short.apply(lambda x: x.sort_values('points').head(10)).reset_index()

        data_short = data_short.groupby(['year'])['duration'].mean().reset_index()

        x_values = np.array(data_short['year'].values.reshape(-1, 1))
        x_values_final = []
        for value in x_values:
            x_values_final.append(value[0])

        y_values = np.array(data_short['duration'].values.reshape(-1, 1))
        y_values_final = []
        for value in y_values:
            y_values_final.append(value[0])
        x_set.append(x_values_final)
        y_set.append(y_values_final)
    return x_set, y_set


def plot_regession_for_each_year(x_values_sets, y_values_sets):
    # Set colors for the regression lines
    colors = ['navy', 'slateblue', 'darkorange', "indigo", "tomato", "red"]
    regressions = ["Top 100", "country", "Dance", "Rock", "R&B", "Latin"]
    
    plt.figure(figsize=(10, 5))

    # Plot the scatter plots and regression lines for each set
    for x_values, y_values, color, regression in zip(x_values_sets, y_values_sets, colors, regressions):
        # Calculate quadratic regression coefficients
        coefficients = np.polyfit(x_values, y_values, 2)

        # Generate x-values for plotting
        x_plot = np.linspace(min(x_values), max(x_values), 1000)

        # Generate regression line values
        regression_line = np.polyval(coefficients, x_plot)

        # Plot the scatter plot
        # plt.scatter(x_values, y_values, label='Data')

        # Plot the regression line
        plt.plot(x_plot, regression_line, color=color, label=regression)
        

    # Set labels for x-axis and y-axis
    plt.xlabel('Year')
    plt.ylabel('Duration in secs')
    

    # Set a title for the graph
    plt.title("Comparison of regression for different Genres")
    

    # Display a legend
    plt.legend(bbox_to_anchor=(1.04, 0.5), loc ="center left", borderaxespad = 0)
    

    # Save plot
    CURRENT_DIR = os.path.dirname(__file__)
    plt.savefig(f"{CURRENT_DIR}/Plots/Comparison_of_regression_for_different_Genres2.png")

    # Display the graph
    plt.show()


CURRENT_DIR = os.path.dirname(__file__)  # Gets directory path of the current python module

all_songs_csv = pd.read_csv(os.path.join(CURRENT_DIR, "Data/Top_100_artists_songs_per_year_with_duration.csv"))
country_csv = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_country_songs_per_year_with_duration.csv'))
dance_csv = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_Dance_songs_per_year_with_duration.csv'))
RnB_csv = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_R&B_songs_per_year_with_duration.csv'))
rock_csv = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_Rock_songs_per_year_with_duration.csv'))
latin_csv = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_Latin_songs_per_year_with_duration.csv'))


x_set, y_set = calculate_mean_each_year([all_songs_csv, country_csv, dance_csv, RnB_csv, rock_csv, latin_csv])
plot_regession_for_each_year(x_set, y_set)
