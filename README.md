# Data analysis of the music charts for the duration of the songs
As part of our course "Data Science with Python and R" at the Technical University of Berlin, we created this project.
The project deals with the analysis of the duration of music. It examines how the duration of music has changed over the past decades. The Billboard top 100 were examined.

## Resources
Music charts - (https://www.billboard.com/charts/hot-100/)


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following libraries

```bash
pip install numpy
pip install pandas
pip install seaborn
pip install matplotlib.pyplot
pip install ast
pip install csv
pip install requests
pip install avgCalculate
pip install scrapy
```

## Usage
### Step 1: Import 

```python
import numpy 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import ast
import csv
import requests
import avgCalculate
```
### Step 2: Scrape Data
The Billboard scraper scrapes the billboard chart and returns a dictionary for each week with the song rank as the key.
To run the scraper you'll need to change your directory to "spiders"
```bash
cd billboard_scraper/billboard/spiders 
```
And then run the command 
```bash
scrapy crawl billboard
```
To run the scraper for the different charts you'll need to change the Parameter billboard_url and Date.

BILLBOARD_URL AND DATE FOR RESPECTIVE GENRE

-Hot 100
```python
billboard_url = "https://www.billboard.com/charts/hot-100/"
date = [1958, 8, 4]
```

-Latin
```python
billboard_url = "https://www.billboard.com/charts/latin-songs/"
date = [1986, 9, 6]
```
-R&B
```python
billboard_url = "https://www.billboard.com/charts/r-and-b-songs/"
date = [2012, 10, 20]
```
-Rock
```python
billboard_url = "https://www.billboard.com/charts/rock-songs/"
date = [2009, 6, 20]
```
-Country
```python
billboard_url = "https://www.billboard.com/charts/country-songs/"
date = [1958, 10, 20]
```
-Dance/Electronic
```python
billboard_url = "https://www.billboard.com/charts/dance-electronic-songs/"
date = [2013, 1, 26]
```


### Step 3: Calculate the yearly/ monthly charts and create a CSV file

Since we want to calculate our results on a yearly or monthly basis, we need to
calculate the top 100 for each year or month from the weekly Hot 100 Billboard songs. 
Futhermore we restructure the scrapted dictonary into a dataframe, which we save 
as a CSV file. 

Therefore run the files 
```bash
calculation_of_top_100_per_year.py
```
and for each month of the years between 2005 and 2023 
```bash
calculation_of_top_100_per_year_month.py 
```
You have to run the files for each txt file you scraped before (different genres, times) once.
To do this change in line 12 the name of the file in the data folder for which you want to calculate the top 100. 
Additionally you have to modify in line 32 the name of the file in which you want to save your results. 
If the file does not exists yet, it will be created by that.

#### Our calculation in steps 
 1. Sum the placings of a song for each year or month 
 2. Songs, which stayed longer in the chart were more successful and therefore add (52 - Number weeks, the song placed in the chart) * 101 
 3. the first 100 songs with the lowest total score are our Top 100 

### Step 4: Add the duration
To add the durations, you must first request a Bearer Token with your credentials:

```bash
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=-INSERT YOUR CLIENT ID HERE-&client_secret=-INSERT YOUR CLIENT SECRET HERE-"
```
Further information: https://developer.spotify.com/documentation/web-api/tutorials/getting-started

Insert your token in the file add_duration.py:
```python
"Authorization": "Bearer -INSERT YOUR TOKEN HERE-"
```

To add the duration to different csv files you'll need to change the parameter "input_file" and "output_file".
```python
input_file = os.path.join(CURRENT_DIR, "./-INSERT A VALID FILENAME.CSV-")
output_file = os.path.join(CURRENT_DIR, "./-INSERT A VALID FILENAME.CSV-")
```

### Step 5: Create plots

We have divided our code for the plots into several files so that it is organized and easier to read. By running each file you can create one to three plots. 
In the following is listed which file creates which plot and which calculations are included. 

If you used different names for the files, in which you saved the calculated top 100 dataframe, 
you need to change the input before you can ran the run code to create the plots. 

- Create the scatter plot with regression of order two for the Top 100 and Top 10 as well as a comparison of the regressions 

     ```bash
          ComparisonTop10AndTop100.py 
     ```
     Line of input: 14

     ##### Calculations: 
      1. Mean duration per year 
      2. Regression of order 2 with x = years and y = mean duration 

- Create line graph with variance of duration of Top 100 per year and line graph with mean and median of durations of Top 100 per year 
     ```bash
          Calculations_of_mean_median_variance_of_top_100.py 
     ```
     Line of input:  13 
     #### Calculations: 
      1. Mean duration of Top 100  per year 
      2. Median of duration of Top 100  per year 
      3. Variance of duration of Top 100 per year 

- Create 
     ```bash

     ```
     Line of input:  
     Calculations: 
      1. 



## Authors and acknowledgment
- @elias_safo
- @marla-studiert
- @segerath052
- @sofika.gega


## Feedback
If you have any feedback, or find any bugs, please let us know just opening an issue.
