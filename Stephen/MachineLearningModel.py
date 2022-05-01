#### Program to Jehnerate local files containing data-sets needed for Training  ####
####    Information pulled from csv file and fit into machine learning model    ####

# Import needed libraries
import os
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegressionCV
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import ARDRegression
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import HuberRegressor
from sklearn.linear_model import QuantileRegressor
from sklearn.linear_model import RANSACRegressor
from sklearn.linear_model import TheilSenRegressor
from sklearn.linear_model import PassiveAggressiveRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.cross_decomposition import PLSRegression
from sklearn.dummy import DummyRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn import preprocessing
import pickle

# Creates the dataframe for training
filename = 'DataSets\out.csv'
names = ['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Volume', 'Change', '50 Day MA', '100 Day MA', '200 Day MA','50 Day Support', '100 Day Support', '150 Day Support', '200 Day Support','50 Day Resistance', '100 Day Resistance', '150 Day Resistance', '200 Day Resistance','50 EMA', '100 EMA', '150 EMA', '200 EMA','50 AVG Gain', '100 AVG Gain', '150 AVG Gain', '200 AVG Gain','50 AVG Loss', '100 AVG Loss', '150 AVG Loss', '200 AVG Loss', 'RSI']
df = pd.read_csv(filename, names=names)
print (df.shape)

# Converts the needed columns to seperate arrays for training and testing
X = np.asarray(df[['50 Day MA', '100 Day MA', '200 Day MA','50 Day Support', '100 Day Support', '150 Day Support', '200 Day Support','50 Day Resistance', '100 Day Resistance', '150 Day Resistance', '200 Day Resistance', '50 EMA', '100 EMA', '150 EMA', '200 EMA','50 AVG Gain', '100 AVG Gain', '150 AVG Gain', '200 AVG Gain','50 AVG Loss', '100 AVG Loss', '150 AVG Loss', '200 AVG Loss', 'RSI']])
Y = np.asarray(df['Change'])

# Splits into training set and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

# Scale Data
scalerX = preprocessing.StandardScaler().fit(X_train)
X_scaled = scalerX.transform(X_train)

scalerY = preprocessing.StandardScaler().fit(X_test)
X_scaledTest = scalerY.transform(X_test)


# Normalizes Data
NormalX = preprocessing.Normalizer().fit(X_train)
X_Normalized = NormalX.transform(X_train)

NormalY = preprocessing.Normalizer().fit(X_test)
X_NormalizeTest = NormalY.transform(X_test)

# LinearRegression
lr = LinearRegression().fit(X_Normalized, y_train)
print(f"LinearRegression: {lr.score(X_NormalizeTest, y_test)}")
filename = "sklearnModels/LinearRegression_Model.sav"
pickle.dump(lr, open(filename, 'wb'))
del lr

# RandomForestRegressor
rfr = RandomForestRegressor().fit(X_scaled, y_train)
print(f"RandomForestRegressor: {rfr.score(X_scaledTest, y_test)}")
filename = "sklearnModels/RandomForestRegressor.sav"
pickle.dump(rfr, open(filename, 'wb'))
del rfr

# RandomForestRegressor
adaBoost = AdaBoostRegressor().fit(X_train, y_train)
print(f"AdaBoostRegressor: {adaBoost.score(X_test, y_test)}")
filename = "sklearnModels/adaBoost.sav"
pickle.dump(adaBoost, open(filename, 'wb'))
del adaBoost

# RandomForestRegressor
bagging = BaggingRegressor().fit(X_Normalized, y_train)
print(f"BaggingRegressor: {bagging.score(X_NormalizeTest, y_test)}")
filename = "sklearnModels/bagging.sav"
pickle.dump(bagging, open(filename, 'wb'))
del bagging

# RandomForestRegressor
extraTree = ExtraTreesRegressor().fit(X_Normalized, y_train)
print(f"ExtraTreesRegressor: {extraTree.score(X_NormalizeTest, y_test)}")
filename = "sklearnModels/extraTree.sav"
pickle.dump(extraTree, open(filename, 'wb'))
del extraTree

# RandomForestRegressor
GradientBoosting = GradientBoostingRegressor().fit(X_Normalized, y_train)
print(f"GradientBoostingRegressor: {GradientBoosting.score(X_NormalizeTest, y_test)}")
filename = "sklearnModels/GradientBoosting.sav"
pickle.dump(GradientBoosting, open(filename, 'wb'))
del GradientBoosting

# RandomForestRegressor
HistGradient = HistGradientBoostingRegressor().fit(X_Normalized, y_train)
print(f"HistGradientBoostingRegressor: {HistGradient.score(X_NormalizeTest, y_test)}")
filename = "sklearnModels/HistGradient.sav"
pickle.dump(HistGradient, open(filename, 'wb'))
del HistGradient

# RandomForestRegressor
pls = PLSRegression().fit(X_Normalized, y_train)
print(f"PLSRegression: {pls.score(X_NormalizeTest, y_test)}")
filename = "sklearnModels/PLSRegression.sav"
pickle.dump(pls, open(filename, 'wb'))
del pls

# RandomForestRegressor
dummy = DummyRegressor().fit(X_train, y_train)
print(f"DummyRegressor: {dummy.score(X_test, y_test)}")
filename = "sklearnModels/DummyRegressor.sav"
pickle.dump(dummy, open(filename, 'wb'))
del dummy

# RandomForestRegressor
GaussianProcess = GaussianProcessRegressor().fit(X_train, y_train)
print(f"GaussianProcessRegressor: {GaussianProcess.score(X_test, y_test)}")
filename = "sklearnModels/GaussianProcess.sav"
pickle.dump(GaussianProcess, open(filename, 'wb'))
del GaussianProcess

# RandomForestRegressor
MLP = MLPRegressor().fit(X_train, y_train)
print(f"MLPRegressor: {MLP.score(X_test, y_test)}")
filename = "sklearnModels/MLPRegressor.sav"
pickle.dump(MLP, open(filename, 'wb'))
del MLP

# RandomForestRegressor
PassiveAggressive = PassiveAggressiveRegressor().fit(X_train, y_train)
print(f"PassiveAggressiveRegressor: {PassiveAggressive.score(X_test, y_test)}")
filename = "sklearnModels/PassiveAggressiveRegressor.sav"
pickle.dump(PassiveAggressive, open(filename, 'wb'))
del PassiveAggressive

# RandomForestRegressor
RANSAC = RANSACRegressor().fit(X_train, y_train)
print(f"RANSACRegressor: {RANSAC.score(X_test, y_test)}")
filename = "sklearnModels/RANSACRegressor.sav"
pickle.dump(RANSAC, open(filename, 'wb'))
del RANSAC

# RandomForestRegressor
Bayesian = BayesianRidge().fit(X_train, y_train)
print(f"BayesianRidge: {Bayesian.score(X_test, y_test)}")
filename = "sklearnModels/BayesianRidge.sav"
pickle.dump(Bayesian, open(filename, 'wb'))
del Bayesian

# RandomForestRegressor
ARD = ARDRegression().fit(X_train, y_train)
print(f"ARDRegression: {ARD.score(X_test, y_test)}")
filename = "sklearnModels/ARDRegression.sav"
pickle.dump(ARD, open(filename, 'wb'))
del ARD

# RandomForestRegressor
SGD = SGDRegressor().fit(X_train, y_train)
print(f"SGDRegressor: {SGD.score(X_test, y_test)}")
filename = "sklearnModels/SGDRegressor.sav"
pickle.dump(SGD, open(filename, 'wb'))
del SGD

# Generate Predicitons
# lrpredictions = lr.predict(X_test)
# rfrpredictions = rfr.predict(X_test)

# Print Predictions
# for i in range(100): #len(lrpredictions)):
    # print(f"LinearRegression Predicted Change: {lrpredictions[i]:0.2f}, Actual Change: {y_test[i]}")
    
# for i in range(100): #len(rfrpredictions)):
    # print(f"RandomForestRegressor Predicted Change: {rfrpredictions[i]:0.2f}, Actual Change: {y_test[i]}")

# saveModel = input("\nWould you like you save a model?(Y/N)")

# if saveModel.lower() == 'y':
    # filename = "finalizedModel.sav"
    # modelChoose = False
    # while modelChoose == False:
        # modelChoice = input('Would you like to save the LinearRegression model (lr) or RandomForestRegressor (rfr) model?')
        # if modelChoice.lower() == 'lr':
            # pickle.dump(lr, open(filename, 'wb'))
            # modelChoose = True
        # elif modelChoice.lower() == 'rfr':
            # pickle.dump(rfr, open(filename, 'wb'))
            # modelChoose = True
        # else:
            # print("Choice not reconized...")
        
            
