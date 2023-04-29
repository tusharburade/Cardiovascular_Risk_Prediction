# Project Title : 
Cardiovascular Risk Prediction

## Description

I started this project by importing data and then i started seeing the each and every column and realizing why the columns important, further i went to analysis the dataset, During the time of analysis, I initially did EDA on all the features of our datset. I first analysed our dependent variable 'TenYearCHD', then next i analysed independent categorical variable and after that independent contineous numerical variables, then i have done some preprocessing on data set and handled the missing data, duplicate data and outliers and also see the distribution of data. Then i have done some encoding of categorical variables.
Next i implemented 4 machine learning algorithms Logisctic Regression, Decision Tree, Random Forest and Adaboost. I also did hyperparameter tuning to improve our model performance, and then i created the API and used the Postman application to see the result.

## Table of Content
* Dataset Information
* Tools and Libraries Used
* Files
* Results
* Screenshots
* Deployment
* Feedback

## Dataset Information
The dataset is from an ongoing cardiovascular study on residents of the town of Framingham,Massachusetts. The classification goal is to predict whether the patient has a 10-year risk offuture coronary heart disease (CHD). The dataset provides the patients’ information. It includes over 4,000 records and 15 attributes.

Dataset Link:-https://raw.githubusercontent.com/samarthgangurde01/Cardiovascular-Risk-Prediction/main/data_cardiovascular_risk.csv

## Tools and Libraries Used
* Pandas
* numpy
* Matplotlib
* Seaborn
* plotly
* sklearn
* imblearn
* pickle

## Files
This repository contain files as mentioned below:

* Cardiovascular_Risk_Prediction.ipynb : .ipynb file contains all the python code, documentation and visualization.

* data_cardiovascular_risk.csv : Our dataset 

* project_data.json : Encoded data and columns names

* requirements.txt :contains required libraries 

* utils.py : Functions required for model Prediction

* config.py : Path of .pkl and .json file

* interface.py : Flask code 

## Results

* Decision tree                  : 0.777286

* adaboost                       : 0.845133

* Decision tree pruining         : 0.848083

* Decision tree hyperparameter   : 0.849558

* Adaboost hyperparameter        : 0.852507

* random forest hyperparameter   : 0.853982

* Random forest                  : 0.856932

* logistic Regression            : 0.858407

## Trial Dataset

id = 1	

age = 36

education = 4.0

sex = "M"	

is_smoking = 'NO'	

cigsPerDay = 0

BPMeds = 0.0

prevalentStroke	= 0

prevalentHyp	= 1

diabetes	= 0

totChol	= 221.0

sysBP	= 168

diaBP	= 98.0

BMI	= 29.77

heartRate	= 72

glucose	= 75

## Feedback

If you have any feedback, please reach out to us at trburade@gmail.com