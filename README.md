# Group 409: Bike Sharing Machine Learning Model
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*__Creators__: Aman Kumar Garg, Victor Cuspinera-Contreras, Yingping Qian*

[Group Project Repo Link](https://github.com/UBC-MDS/DSCI_522_Group_409)

## 1. Dataset

The dataset we are using to build a machine learning model is the bike sharing dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset). It contains both the hourly and daily data about the numbers of bike rentals in Washington, DC between 2011 and 2012. For this project, only the hourly data is used.

The dataset has 1 target `cnt` and 16 features, including both time and weather-related information for each hour on a specific day.  All the features and target are listed below:
1. `instant`: Record index
2. `dteday`: Date
3. `season`: Season (1:spring, 2:summer, 3:fall, 4:winter)
4. `yr`: Year (0: 2011, 1:2012)
5. `mnth`: Month 
6. `hr`: Hour
7. `holiday`: (0: No, 1: Yes)
8. `weekday`: Day of the week (starting from 0: Sunday)
9. `workingday`: (0: No, 1: Yes)
10. `weathersit`: 
  - 1: Clear, Few clouds, Partly cloudy, Partly cloudy. 
  - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist. 
  - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds. 
  - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
11. `temp`: Normalized temperature in Celsius.
12. `atemp`: Normalized feeling temperature in Celsius. 
13. `hum`: Normalized humidity.
14. `windspeed`: Normalized wind speed.
15. `casual`: count of casual users
16. `registered`: count of registered users
17. `cnt`: count of total rental bikes including both casual and registered

The dataset could be downloaded using the [data_download.py script](https://github.com/UBC-MDS/DSCI_522_Group_409/blob/master/src/data_download.py) in our repository. Data splitting is also done in this download script.

This dataset is obtained from the University of California Irvine Machine learning Repository [1]. 

> References 
>[1] Hadi Fanaee-T 
> Laboratory of Artificial Intelligence and Decision Support (LIAAD), University of Porto INESC Porto, Campus da FEUP 
Rua Dr. Roberto Frias, 378 4200 - 465 Porto, Portugal 
> Original Source: http://capitalbikeshare.com/system-data 
> Weather Information: http://www.freemeteo.com 
> Holiday Schedule: http://dchr.dc.gov/page/holiday-schedule


## 2. Research Question

Demand forecast is an important aspect for many companies in carrying out their operations. In our case, with the help of demand forecasting, bike rental company can perform many tasks such as inventory management (no. of bikes), man power management etc. Such planning will result in making operations efficient and effective. Planning and forecasting can help in facing the sudden challenges and problems in a much better way.

The main research question of our proposal is around building such demand forecasting model, which is as follows.

- **Given the information shared by Bike share company, can we predict the count of bike rentals on hourly basis in order to forecast the future demand?**

There are many other areas that we can explore around our main research question. We would to know what are the strong predictors that can help in predicting the future demand for the bike rentals. Through EDA, we are trying to see the the trend of count of bike rentals with hr, weekday and temperature.

<p align="center">
<img src="img/bike_rental.jpg" alt="Markdown Monster icon" style="float: left; margin-right: 10px;" height= "400" width= "400" align="middle"/>
</p>


## 3. Methodology

In order to answer our main research question, we are planning to explore different machine learning algorithms. The data shared by the Bike Rider Company is quite cleaned and does not require much data manipulation. Since our problem is `regression`, we can potentially work with linear regression, KNN, Random Forest and SVR. We have selected `mean squared error` as the criteria to select the best model among the selected models.      

In the [EDA File](https://github.com/UBC-MDS/DSCI_522_Group_409/blob/master/eda/EDA.ipynb), we have checked if there is any null values present in the data. Moreover, we have done data profiling and get the statistical information such as mean, median, min, max and quartiles of the continuous variables of the data. We have also built many visualizations such as heat maps and point graphs to deep dive into the data.      

