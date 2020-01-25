Group 409: Bike Sharing Machine Learning Model
================

[![License:
MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

***Creators**: Aman Kumar Garg, Victor Cuspinera-Contreras, Yingping
Qian*

[Group Project Repo Link](https://github.com/UBC-MDS/DSCI_522_Group_409)

## 1\. Dataset

The dataset we are using to build a machine learning model is the bike
sharing dataset from [UCI Machine Learning
Repository](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset).
It contains both the hourly and daily data about the numbers of bike
rentals in Washington, DC between 2011 and 2012. For this project, only
the hourly data is used.

The dataset has 1 target `cnt` and 16 features, including both time and
weather-related information for each hour on a specific day. All the
features and target are listed below:  

1. `instant`: Record index 
2.`dteday`: Date  
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

The dataset could be downloaded using the [data\_download.pyscript](https://github.com/UBC-MDS/DSCI_522_Group_409/blob/master/src/data_download.py) in our repository. Data splitting is also done in this download script.

The command to download the data is as follows:

`python3.6 data_download.py --file_url="https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip" --file_path="home/project/data"`

The file path can be changed according to the desired path.

The dataset used in this project is created by Dr. Hadi Fanaee-T (2013) at Laboratory of Artificial Intelligence and Decision Support (LIAAD), University of Porto INESC Porto. It was sourced from the UCI Machine Learning Repository and can be found [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00275/).

## 2\. Research Question

Demand forecasting is an important aspect for many companies in carrying out their operations. In our case, with the help of demand forecasting, bike rental company can perform many tasks such as inventory management (no. of bikes), man power management etc. Such planning will result in making operations efficient and effective. Planning and forecasting can help in facing the sudden challenges and problems in a much better way.

The main research question of our proposal is to build an effective demand forecasting model and the predictive question is as follows.

  - **Given the information shared by Bike share company, can we predict the count of bike rentals on hourly basis in order to forecast the future demand of bike rentals?**

There are many other areas that we can explore around our main research question. We would to know what are the strong predictors that can help in predicting the future demand for the bike rentals(i.e. predictive question). Through EDA, we are trying to see the the trend of count of bike rentals with hr, weekday and temperature.

<p align="center">

<img src="img/bike_rental.jpg" alt="Markdown Monster icon" style="float: left; margin-right: 10px;" height= "400" width= "400" align="middle"/>

</p>

## 3\. Methodology

In order to answer our main research question, we are planning to explore different machine learning algorithms. Before building our machine learning models, we will split the data into train and test sets (i.e. 80% train, 20% test) and perform exploratory data analysis to
explore whether any features that are not related to our questions or similar with another feature so that we can remove them from our analysis.

The data shared by the Bike Rider Company is quite cleaned and does not require much data manipulation. Since our problem is `regression`, we can potentially work with `linear regression`, `KNN`, `Random Forest`, `SVR` and few other similar models. We have selected `mean squared error` as the criteria to select the best model among the selected models.

## 4\. Exploratory data analysis

In the [EDA File](https://github.com/UBC-MDS/DSCI_522_Group_409/blob/master/eda/EDA.ipynb), we have checked if there is any null values present in the data. Moreover, we have done data profiling and get the statistical information such as mean, median, min, max and quartiles of the continuous variables of the data. We have also built many visualizations such as heat maps and point graphs to deep dive into the data.

In order to make exploratory data analysis in the EDA we present a table for the matrix of correlations, where we find which variables are related with each other, as well as the explanatory variables with higher correlation with the target variable (number of bike rented), standing out the temperature and hour of the day. One of the most interesting figures is related with the analysis of temperature on bike rental count, which in short shows how the demand for bikes increases when weather is warmer and decreases when the temperatures is lower.

## 5\. Presentation of results

We could share the results of the analysis in different formats in function of the type of information: while we will present in tables the results from the comparison of the different models that can potentially work (`linear regression`, `KNN`, `Random Forest`, `SVR`, among others).
We will select our final model and re-fit the model on the train set and evaluate the performance on the test set. The results of both train and test accurary for the final model will be reported as a table in our final report. We will also present plots and figures as part of our analysis and results in the final report to explain and backup model to
forcast the future demand of bike rentals.

## Dependencies
```
pandas==0.24.2  
numpy==1.16.4  
sklearn==0.22  
altair==3.2.0  
docopt==0.6.2 
```

## License

The Bike Sharing Dataset materials here are licensed as `CC0: Public Domain`. If re-using/re-mixing please provide attribution and link to this webpage.

## References

<div id="refs" class="references">

<div id="ref-uic_repo">
Dua, Dheeru and Graff, Casey. 2017. UCI Machine Learning Repository.
University of California, Irvine, School of Information and Computer 
Sciences.
<http://archive.ics.uci.edu/ml>
</div>

<div id="ref-hadi">
Fanaee-T, Hadi. 2013. “Bike Sharing Dataset Data Set.” University of
Porto, INESC Porto, Campus da FEUP, Rua Dr. Roberto Frias, 378, 4200 -
465 Porto, Portugal: Laboratory of Artificial Intelligence; Decision
Support (LIAAD); Machine, Learning Repository, UCI.  
<https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset>
</div>

<div id="ref-docopt">
Keleshev, Vladimir. 2014. docopt: Command-line interface description 
language. Python package version 0.6.2}.
<https://github.com/docopt/docopt>
</div>

<div id="ref-pandas">
McKinney, Wes and others. 2010. Pandas. Data structures for statistical 
computing in python, Proceedings of the 9th Python in Science Conference}, 
volume 445, pages 51--56, Austin, TX.
</div>

<div id="ref-numpy">
Oliphant, Travis E. 2006. A guide to NumPy. Volume=1, publisher Trelgol 
Publishing, USA.
</div>

<div id="ref-altair">
Pedregosa, F., Varoquaux, G., Et Al. 2011. Scikit-learn: Machine 
Learning in Python. Journal of Machine Learning Research, volume 12, 
pages 2825--2830.
</div>

<div id="ref-altair">
VanderPlas, J., Granger, B., Et All. 2018. Altair: Interactive
Statistical Visualizations for Python. The Journal of Open Source 
Software, volume 3, number 32.
<http://idl.cs.washington.edu/papers/altair>
</div>

</div>
