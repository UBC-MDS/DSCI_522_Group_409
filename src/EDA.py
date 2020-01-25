# author: Aman Kumar Garg, Victor Cuspinera-Contreras, Yingping Qian 
# date: 2020-01-22

'''This script takes a document with it's filepath and returns a file
with the the Exploratory Data Analysis (EDA) in the desired folder.

Usage: src/EDA.py --input_file=<input_file> --output_path=<output_path>

Options:
--input_file=<input_file>  Path including the filename that contains the input file.
--output_path=<output_path>  Path (excluding filename) to the folder.
'''

import numpy as np
import pandas as pd
import altair as alt
import seaborn as sns
pd.set_option("display.max_colwidth", 200)
alt.data_transformers.disable_max_rows()
from scipy.stats import pearsonr
from docopt import docopt
import requests, io, os

opt = docopt(__doc__)

def main(input_file, output_path):
    
    # 0. TEST output_path EXISTS
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)
    
    # 1. DESCRIBE THE DATASET
    # The dataset we chose is the Bike Sharing Dataset from 
    # UCI machine learning repository. This dataset contains
    # the hourly and daily count of rental bikes in 2011 and
    # 2012 in Capital bikeshare system in Washington, DC with
    # the corresponding weather and seasonal information. 
    
    # 2. LOAD THE DATASET
    bike_data = pd.read_csv(input_file)

    # 3. EXPLORE THE DATASET
    table_descr = bike_data.describe()
    table_descr.to_csv(output_path + "/tab_1.csv", index = True)
    
    # 3.1 Printing description
    print("\nThe dataframe columns are: ", list(bike_data.columns))
    month_list = sorted(list(bike_data['mnth'].unique()))
    print("\nGeneral information about the dataset:")
    print("- The month ranges from {0} to {1}, which represents the {2} months of the year.".format(month_list[0],
          month_list[-1],
          len(month_list)))
    hour_list = sorted(list(bike_data['hr'].unique()))
    print("- The hour ranges from {0} to {1}, that represents the {2} hours of the day.".format(hour_list[0],
          hour_list[-1],
          len(hour_list)))
    print("- The holiday type contains: ", list(bike_data['holiday'].unique()))
    weekdays = sorted(list(bike_data['weekday'].unique()))
    print("- The weekday type contains: ", weekdays)
    print("- The workingday type contains: ", sorted(list(bike_data['workingday'].unique())))
    print("- The weather type contains: ", list(bike_data['weathersit'].unique()))
    temp_list = sorted(list(bike_data['temp'].unique()))
    print("- The normalized tempereature ranges from {0} to {1}".format(temp_list[0],
          temp_list[-1]))
    hum_list = sorted(list(bike_data['temp'].unique()))
    print("- The normalized humidity ranges from {0} to {1}".format(hum_list[0],
          hum_list[-1]))
    wind_list = sorted(list(bike_data['windspeed'].unique()))
    print("- The normalized windspeed ranges from {0} to {1}".format(wind_list[0],
          wind_list[-1]))
    cnt_list = sorted(list(bike_data['cnt'].unique()))
    print("- The target count of bike rentals ranges from {0} to {1}".format(cnt_list[0],
          cnt_list[-1]), "users.\n")
    
    # 3.2 Checking the Null Values in the dataset
    sns.set(rc={'figure.figsize':(6,5)})
    chart_nulls = sns.heatmap(bike_data.isnull(), cmap='viridis', 
                      cbar=False).get_figure().savefig(output_path + "/fig_1_nulls.png")

    # 4. INITIAL TOUGHTS
    # - The original dataset has 17 variables with 13,903 observations,
    #   but not all variables would be useful for the model.
    # - Operation is 24 hr even on weekends and holidays.
    # - `temp` and `atemp` are normalized with different scales, which 
    #   can be confusing to interpret.
    
    # 5. WRANGLING
    # Almost all the wran will be done in a different script.
    bike_data_2 = bike_data.groupby(['weekday', 'hr']).mean().reset_index()
    bike_data_2
    
    # 6. RESEARCH QUESTION
    # Main:
    # - Given the information shared by Bike share company, can we predict
    #   the count of bike rentals in order to forecast the future demand?
    #
    # Sub-question:
    # - Identify the strongest predictors that can help in predicting the 
    #   future demand for bike rentals. (predictive)
    # - Identify the regression model that would have a better performance
    #   to predict the future demand for bike rentals. (predictive)
    
    # 7. DATA ANALYSIS AND VISUALIZATIONS
    # 7.1 Analysis of temp on bike rental count
    order_of_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                     'Friday', 'Saturday', 'Sunday']
    
    chart_temp = alt.Chart(bike_data).mark_point(opacity=0.3, size = 4).encode(
                alt.X('temp:Q'),
                alt.Y('cnt:Q'),
                color = alt.Color('weekday:N', legend=None)
            ).properties(title="Temp vs Bike Rental",
                        width=200, height=150
            ).facet(alt.Facet('weekday:N', 
                              sort = order_of_days),
                    columns=3
            ).configure_axisX(labelFontSize=12,
                            titleFontSize=15
            ).configure_axisY(labelFontSize=12,
                            titleFontSize=15
            ).configure_title(fontSize=17)
    chart_temp.save(output_path + "/fig_2_temp.png", scale_factor=2.0)
    
    # 7.2 Analysis of hour and weekday on bike rental count
    heat_map = alt.Chart(bike_data_2).mark_rect().encode(
                    x = alt.X("hr:O", 
                              title = "Hour of Day", 
                              axis = alt.Axis(labelAngle = 0)),
                    y = alt.Y('weekday:O',
                              sort=order_of_days,
                              title = "Day of Week"),
                    color=alt.Color('cnt:Q', 
                                    legend=alt.Legend(title = "counts")),
                    tooltip=['weekday', 'hr', 'cnt']
                ).properties(title = "Count of bike rental by Hour and Day in Washington, DC")
    heat_map.save(output_path + "/fig_3_hr.png", scale_factor=2.0)
    
    # 7.3 Analysis of weather and humidity on demand for rental bikes
    chart_weather = alt.Chart(bike_data).mark_point(opacity=0.5, size = 4).encode(
                alt.X('hum:Q'),
                alt.Y('cnt:Q'),
                color = alt.Color('weathersit:N', legend=None)
            ).properties(title="Temp vs Bike Rental",
                        width=200, height=150
            ).facet(alt.Facet('weathersit:N', 
                              sort = order_of_days),
                    columns=2
            ).configure_axisX(labelFontSize=12,
                            titleFontSize=15
            ).configure_axisY(labelFontSize=12,
                            titleFontSize=15
            ).configure_title(fontSize=17)
    chart_weather.save(output_path + "/fig_4_weather.png", scale_factor=2.0)
    
    # 7.4 Correlation matrix
    sns.set(rc={'figure.figsize':(11,11)})
    corrMatrix = bike_data.corr()
    sns.heatmap(corrMatrix, annot=True,
            cmap="GnBu").get_figure().savefig(output_path + "/fig_5_corr.png", dpi=400)
    
    # 8. REFERENCES

def check_file(file_path):
    """
    Writing the text file and print success in the file
    """
    if not os.path.exists(file_path):
        os.makedirs(file_path, exist_ok=True)
    
    file1 = open(file_path + "/success.txt","w")#write mode 
    file1.write("Succes Download Figures") 
    file1.close()
    return os.path.isfile(file_path +  "/success.txt")
    
def test_error(file_path):
    assert check_file(file_path), "Training file is not generated"

test_error(opt["--output_path"])

if __name__ == "__main__":
    main(opt["--input_file"], opt["--output_path"])
