"""
Creates a scatter plot with a regression of order two of the top 100 songs
each year for the genres Dance, R & B, Country, Rock and Latin. 
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


"""def plot_regession_for_each_year(x_values_sets, y_values_sets):

    # Generate x-values for plotting
    x_plot = np.linspace(min(x_values), max(x_values), 100)

    # Generate regression line values
    regression_line = np.polyval(coefficients, x_plot)

    # Plot the scatter plot
    # plt.scatter(x_values, y_values, label='Data')

    # Plot the regression line
    plt.plot(x_plot, regression_line, color="black")

# Set labels for x-axis and y-axis
    plt.xlabel('Years')
    plt.ylabel('Duration in secs')

    # Set a title for the graph
    plt.title("Mean Duration Top 100 Songs Per Year With Regression")

    # Display a legend
    plt.legend()

    # Save plot
    CURRENT_DIR = os.path.dirname(__file__)
    plt.savefig(f"{CURRENT_DIR}/Plots/Comparison_of_regression_for_different_Genres.png")"""


def create_combined_scatter_plots(x_values, y_values, Plot_names, color):
    num_plots = len(x_values)
    rows = int(num_plots / 2) + num_plots % 2
    cols = 2

    fig, axes = plt.subplots(rows, cols, figsize=(10, 6))
    fig.tight_layout(pad=5.0)

    for i, ax in enumerate(axes.flat):
        if i < num_plots:
            ax.scatter(x_values[i], y_values[i])
            ax.set_xlabel('Years')
            ax.set_ylabel('Duration in secs')
            ax.set_title(f'Scatter Plot {Plot_names[i]}')

            # Calculate regression line parameters
            regression_params = np.polyfit(x_values[i], y_values[i], 2)
            regression_line = np.polyval(regression_params, x_values[i])

            # Plot regression line
            ax.plot(x_values[i], regression_line, color=color[i], label='Regression Line')

        # Save plot
    CURRENT_DIR = os.path.dirname(__file__)
    plt.savefig(f"{CURRENT_DIR}/Plots/Scatter_plot_for_different_Genres.png")
    plt.show()


CURRENT_DIR = os.path.dirname(__file__)  # Gets directory path of the current python module

all_songs_csv = pd.read_csv(os.path.join(CURRENT_DIR, "Data/Top_100_artists_songs_per_year_with_duration.csv"))
country_csv = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_country_songs_per_year_with_duration.csv'))
dance_csv = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_Dance_songs_per_year_with_duration.csv'))
RnB_csv = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_R&B_songs_per_year_with_duration.csv'))
rock_csv = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_Rock_songs_per_year_with_duration.csv'))
latin_csv = pd.read_csv(os.path.join(CURRENT_DIR, 'Data/Top_100_Latin_songs_per_year_with_duration.csv'))
x_set, y_set = calculate_mean_each_year([all_songs_csv, RnB_csv, dance_csv, country_csv, rock_csv, latin_csv])
Plot_names = ["All Genres", "R&B Genre", "Dance/Electronic Genre", "Country Genre", "Rock Genre", "Latin Genre"]
colors = ['navy', "tomato", 'darkorange', 'slateblue', "indigo", "red"]

create_combined_scatter_plots(x_set, y_set, Plot_names, colors)
