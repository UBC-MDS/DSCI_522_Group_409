# author: Aman Kumar Garg, Victor Cuspinera-Contreras, Yingping Qian 
# date: 2020-01-24

'''This script runs the model on training data. This script takes a filepath of the 
training data and save the output in the desired folder.

Usage: src/data_modelling.py --input_file_path=<input_file_path> --output_file_path=<output_file_path>

Options:
--input_file_path=<input_file_path>  Path (excluding filename) to the folder
--output_file_path=<output_file_path>  Path (excluding filename) to the folder.
'''

import os
import ast
import numpy as np
import pandas as pd
from docopt import docopt
# classifiers / models
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV, cross_val_score
from sklearn.metrics import r2_score
import time
import altair as alt

from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.pipeline import Pipeline


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler





opt = docopt(__doc__)

def main(input_file_path, output_file_path):

    if not os.path.exists(output_file_path):
        os.makedirs(output_file_path, exist_ok=True)
        
    #Input training and tesing data
    training_data = pd.read_csv(input_file_path + "/training_data.csv")
    testing_data = pd.read_csv(input_file_path + "/test_data.csv")

    training_data['weekday'] = training_data['weekday'].replace(
                                {'Sunday' : 0,
                                 'Monday' : 1,
                                 'Tuesday' : 2,
                                 'Wednesday' : 3,
                                 'Thursday' : 4,
                                 'Friday' : 5,
                                 'Saturday' : 6})


    testing_data['weekday'] = testing_data['weekday'].replace(
                                {'Sunday' : 0,
                                 'Monday' : 1,
                                 'Tuesday' : 2,
                                 'Wednesday' : 3,
                                 'Thursday' : 4,
                                 'Friday' : 5,
                                 'Saturday' : 6})


    # segregating numerical column names and putting them in the list  
    numeric_features = ['temp','atemp','hum','windspeed']

    # categorical numerical column names and putting them in the list 
    categorical_features = ['holiday','workingday']

    # Prepocessing 
    preprocessor = ColumnTransformer(
    transformers=[
        ('scale', MinMaxScaler(), numeric_features),
        ('ohe', OneHotEncoder(drop="first"), categorical_features)])\
    

    X_train = pd.DataFrame(preprocessor.fit_transform(training_data),
                       index=training_data.index,
                       columns=(numeric_features +
                                list(preprocessor.named_transformers_['ohe']
                                     .get_feature_names(categorical_features))))


    X_test = pd.DataFrame(preprocessor.transform(testing_data),
                       index=testing_data.index,
                       columns=(numeric_features +
                                list(preprocessor.named_transformers_['ohe']
                                     .get_feature_names(categorical_features))))

    

    X_train['season'] = training_data['season']
    X_train['mnth'] = training_data['mnth']
    X_train['hr'] = training_data['hr']
    X_train['weekday'] = training_data['weekday']
    X_train['weathersit'] = training_data['weathersit']


    X_test['season'] = testing_data['season']
    X_test['mnth'] = testing_data['mnth']
    X_test['hr'] = testing_data['hr']
    X_test['weekday'] = testing_data['weekday']
    X_test['weathersit'] = testing_data['weathersit']


    y_train = training_data['cnt']
    y_test = testing_data['cnt']

    #Models to tune
    model_list = [LinearRegression(), KNeighborsRegressor(), RandomForestRegressor()]
    model = ["LinearRegression","KNN","RandomForest"]

    #Hyperparameters to tune
    parameter_list = [{"normalize":[True,False]},
                     {'n_neighbors':[1, 5, 10, 15,20]},
                     {'max_depth':[10,15,20],'n_estimators':[50,100,200]}]

    #Model and Hyperparameter Tuning
    data_combine = pd.DataFrame()
    data_result = pd.DataFrame()
    print ("Tuning Start")
    for i in range(3):
        t = time.time()
        print(i)
        train_error, test_error, grid_test_error,best_parameters, y_pred, train_r2_error, test_r2_error = model_train(model_list[i],parameter_list[i],X_train, 
                                                                                   y_train, X_test, y_test, )
        
        
        data_result = pd.concat([data_result,pd.DataFrame({"model":[model[i]],"test_error":[test_error],
                                                          "train_error":[train_error],"test_r2_error":[test_r2_error],"train_r2_error":[train_r2_error],"best_param":[best_parameters],"grid_test_error":[grid_test_error],
                                                           "Computational Time (sec)":time.time()-t})])
        
        data_combine = pd.concat([data_combine,pd.DataFrame({"y_true_test":y_test,"y_predict":y_pred,
                                    "model":model[i]})])


    print ("Tuning Finish")
    data_result = data_result[['model','train_error','test_error',"train_r2_error", "test_r2_error",'best_param', "Computational Time (sec)"]]
    data_result.columns = ['Model','Train Error','Test Error',"Train r2 score", "Test r2 score",'Best Parameters', "Computational Time (sec)"]

    data_result.reset_index(inplace = True)
    data_result.to_csv(output_file_path + "/result.csv", index=False)

    data_combine_rf = data_combine.query("model == 'RandomForest'")

    chart = alt.Chart(data_combine_rf).mark_point(opacity=0.3, size = 4).encode(
            alt.X('y_predict:Q', title = 'Predict Rides'),
            alt.Y('y_true_test:Q', title = 'Actual Rides')
        ).properties(title="Actual Rides vs Predicted Rides",
                    width=550, height=250, background='white').configure_axisX(labelFontSize=12,
    titleFontSize=15).configure_axisY(labelFontSize=12,
    titleFontSize=15).configure_title(fontSize=17).configure_axis(
    grid=False
)

    chart.save(output_file_path + "/fig_result.png", scale_factor=2.0)

    res = ast.literal_eval(data_result.loc[2,"Best Parameters"])

    model = RandomForestRegressor(max_depth = res['max_depth'], n_estimators = res['n_estimators'])
    model.fit(X_train, y_train)
    data_importance = pd.DataFrame({"Features":X_train.columns, "Feature Importance":model.feature_importances_})
    
    chart1 = alt.Chart(data_importance).mark_bar().encode(
    x=alt.X('Feature Importance:Q'),
    y=alt.Y('Features:O', sort=alt.EncodingSortField(field="Feature Importance", op="sum", order='descending'))
    ).properties(title="Importance of Predictors for predicting bike riders",
                    width=550, height=350, background='white').configure_axisX(labelFontSize=12,
    titleFontSize=15).configure_axisY(labelFontSize=12,
    titleFontSize=15).configure_title(fontSize=17)

    chart1.save(output_file_path + "/feature_importance.png", scale_factor=2.0)


def model_train(model,parameters,X_train, y_train, X_test, y_test):

   
    """
    
    Returns the training and testing errors of the input model on the training and testing data after applying hyperparameter tuning.     
        
    Parameters:
    ------
    model: object
    the input ML model
    
    X_train : numpy.ndarray
    the training data
    y_train : numpy.ndarray
    the target of training data
    X_test : numpy.ndarray
    the validation data
    y_test : numpy.ndarray
    the target of validation data
    
    mode : str
    regression or classification
    
        
    Returns:
    -------
    training and testing error, r2 score for training and testing, best hyperparameter: (list)
        
        
       
    """

    #Gridsearch
    clf = GridSearchCV(model, parameters, cv=5, scoring = 'neg_mean_squared_error')
    clf.fit(X_train, y_train)
    
    grid_test_error = np.sqrt(-1*clf.score(X_test, y_test))
    train_error = np.sqrt(mean_squared_error(y_train, clf.predict(X_train)))
    test_error = np.sqrt(mean_squared_error(y_test, clf.predict(X_test)))

    train_r2_error = r2_score(y_train, clf.predict(X_train))
    test_r2_error = r2_score(y_test, clf.predict(X_test))
    
    best_parameters = str(clf.best_params_)
    
                             
    return (train_error,test_error,grid_test_error,best_parameters,np.squeeze(clf.predict(X_test)), train_r2_error, test_r2_error)

def check_file(file_path):
    """
    Writing the text file and print success in the file
    """
    if not os.path.exists(file_path):
        os.makedirs(file_path, exist_ok=True)
        
    file1 = open(file_path + "/success.txt","w")#write mode 
    file1.write("Succes Download") 
    file1.close()
    return os.path.isfile(file_path +  "/success.txt")

def test_error(file_path):
    assert check_file(file_path), "Training file is not generated"


if __name__ == "__main__":
    main(opt["--input_file_path"], opt["--output_file_path"])
    test_error(opt["--input_file_path"])




