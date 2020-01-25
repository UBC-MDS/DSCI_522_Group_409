---
title: "Bike Sharing Machine Learning Model"
author: "Aman Kumar Garg, Victor Cuspinera-Contreras, Yingping Qian"
date: "24/01/2020 (updated: 2020-01-25)"
always_allow_html: true
output: 
  html_document:
    keep_md: true
    toc: true
bibliography: references.bib
---



# Summary

# Introduction
Demand forecasting is an important aspect for many companies in carrying out their operations. In our case, with the help of demand forecasting, bike rental company can perform many tasks such as inventory management (no. of bikes), man power management etc. Such planning will result in making operations efficient and effective. Planning and forecasting can help in facing the sudden challenges and problems in a much better way.

Here we ask whether we can predict the count of bike rentals on hourly basis in order to forecast the furture demand of bike rentals given the information shared by Bike Share Company. Also, we want to find the strong predictors that can help in predicting the future demand for the bike rentals. 

# Methods

## Data
The dataset we are using to build a machine learning model is the bike sharing dataset from UCI Machine Learning Repository. It contains both the hourly and daily data about the numbers of bike rentals in Washington, DC between 2011 and 2012. We would use the hourly dataset, which is more complete and have a greater number of observations than the daily dataset.The dataset has 1 target and 16 features, including both time and weather-related information for each hour on a specific day. 

The dataset was created by Dr. Hadi @hadi from the Laboratory of Artificial Intelligence and Decision Support (LIAAD), at the @uic_repo.

We have performed an explanatory data analysis (EDA), the full report can be found [here](https://github.com/UBC-MDS/DSCI_522_Group_409/blob/master/eda/EDA_summary.md). In this analysis we  built some visualizations to deep dive the data and found the relationships between different variables, as well as the explanatory variables with higher correlation with the target variable (number of bike rented). As we can see from the plot below, the demand for bikes increases when weather is warmer and decreases when the temperatures is lower.
  
<div class="figure">
<img src="../img/fig_2_temp.png" alt="Figure 1. Analysis of temperatures by weekday" width="65%" />
<p class="caption">Figure 1. Analysis of temperatures by weekday</p>
</div>

<br>
<div class="figure">
<img src="../img/fig_3_hr.png" alt="Figure 2. Analysis per hour and weekday" width="70%" />
<p class="caption">Figure 2. Analysis per hour and weekday</p>
</div>

## Analysis




# Results & Discussion

To make the prediction model, it is required to test different models and check which model fits best. There are several methods available to check which model is best suited for the bike rental data. For this problem, we have used `mean_squared_error` and calculated the error for both training and testing error as shown below. Moreover, we have also tuned hyperparameters to get the best model with best hyperparameters.   
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>Table 1. Training and Testing error for k-nearest neighbors, RandomForest and Linear Regression.</caption>
 <thead>
  <tr>
   <th style="text-align:right;"> index </th>
   <th style="text-align:left;"> Model </th>
   <th style="text-align:right;"> Train.Error </th>
   <th style="text-align:right;"> Test.Error </th>
   <th style="text-align:left;"> Best.Parameters </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:left;"> LinearRegression </td>
   <td style="text-align:right;"> 147.90577 </td>
   <td style="text-align:right;"> 145.60746 </td>
   <td style="text-align:left;"> {'normalize': False} </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:left;"> KNN </td>
   <td style="text-align:right;"> 72.18613 </td>
   <td style="text-align:right;"> 78.42565 </td>
   <td style="text-align:left;"> {'n_neighbors': 15} </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:left;"> RandomForest </td>
   <td style="text-align:right;"> 63.73418 </td>
   <td style="text-align:right;"> 70.39487 </td>
   <td style="text-align:left;"> {'max_depth': 10, 'n_estimators': 200} </td>
  </tr>
</tbody>
</table>

As we can see above, `Random Forest` is the best model with minimum training and testing error. By hyperparameter tuning, we get max depth as 10 and the number of estimators as 100. 

It is possible to see the feature importance through random forest regression. We have plotted the feature importance for all the features as shown below.

<div class="figure">
<img src="../result/feature_importance.png" alt="Figure 3: The plot for importance for predictors." width="85%" />
<p class="caption">Figure 3: The plot for importance for predictors.</p>
</div>

The variable `hr` is the most important feature to predict bike ridership. The second most important feature is temperature. It is also interesting to know if it is a working day or not which also matters in predicting number of bike rentals.

In order to visualise the results, we also plotted the point graph between actual rides and predicted rides. The predicted rides are from test data set using the best model i.e `Random Forest`   

<div class="figure">
<img src="../result/fig_result.png" alt="Figure 4: The plot for predicted and actual rides" width="85%" />
<p class="caption">Figure 4: The plot for predicted and actual rides</p>
</div>

The relationship is looking very linear which means that predicted values are close to the actual values. The model can be used to predict the ridership in the future given the input features.   


# References
