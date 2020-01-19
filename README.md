# Group 409: Bike Sharing Machine Learning Model
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*__Creators__: Aman Kumar Garg, Victor Cuspinera-Contreras, Yingping Qian*

[Group Project Repo Link](https://github.com/UBC-MDS/DSCI_522_Group_409)

## Proposal
---

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
  1: Clear, Few clouds, Partly cloudy, Partly cloudy
  2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
  3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
  4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog)
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
