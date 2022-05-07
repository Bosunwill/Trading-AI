from __future__ import absolute_import, division, print_function

import pathlib
import yfinance as yf
from datetime import datetime, timedelta

import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

import pandas as pd
import seaborn as sns
import numpy as np
import csv

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# GailLossThreshold is used to filter out stocks predicted by the Gain/Loss Classifier to do poorly
# Other Functions them return based on the Prediction Model

# RetrieveListFromFile(filename) Uses the csv file specified to return a list of tickers and predictions

# DailyListNasdaq(GainLossThreshold) Uses the csv file for Nasdaq tickers to return a list of top predicted Stocks

# PredictFromFile(Filename, GainLossThreshold) Uses a filename to return a list of top predicted Stocks

# PredictList(TickerList, GainLossThreshold) Takes a list and creates the stock predicions

# GainLossFromTicker(Ticker) predicts if a stock will gain or loose
#     closer to 1 is stronger prediction to gain while closer to 0 is greater chance to loose

# PredictFromTicker(Ticker) returns to numeric prediction of the percent of gain or loss

# DataFrameFromData(dataSet) creates a dataframe to be used from given data dataset

# CreateDataSetForTicker(Ticker) creates a dataset for a specific ticker

# BubbleSort(SortingList) takes a list of lists where index 0 is the ticker and index 1 is the value to sort by

def RetrieveListFromFile(filename):
    with open(filename, 'r') as readObj:
        csvReader = csv.reader(readObj)
        listOfRows = list(csvReader)
    return listOfRows

def DailyListNasdaq(GainLossThreshold):
    with open('DailyList.csv', 'w') as f:
        f.truncate(0)
    PredictedList = PredictFromFile('nasdaq.csv', GainLossThreshold)
    for i in range(len(PredictedList)):
        with open('DailyList.csv', 'a') as f:
            f.write(f"{PredictedList[i][0]}, {PredictedList[i][1]}\n")

def PredictFromFile(Filename, GainLossThreshold):    
    TickerList = []
    with open(Filename, newline='') as tickerFile:
        reader = csv.reader(tickerFile)
        stockList = list(reader)
        for stock in stockList:
            TickerList.append(stock[0])
    return PredictList(TickerList, GainLossThreshold)

def PredictList(TickerList, GainLossThreshold):
    # Load Models
    gainLossModel = tf.keras.models.load_model('saved_model/stockTFGainLossModel.h5')
    predictModel = tf.keras.models.load_model('saved_model/stockTFmodel.h5')
    gainLossList = []
    returnList = []

    #Cycle Through List
    for i in range(len(TickerList)):        
        # Create a dataset for ticker
        try:
            dataSet = CreateDataSetForTicker(TickerList[i])
            
            # Creates the dataframe from data
            df = DataFrameFromData(dataSet)
            Close = df.pop('Close')
            
            # Predicts Models
            gainLoss = gainLossModel.predict(df)
            predictionPercent = (predictModel.predict(df) / Close[0]) * 100

            # Converts to floats
            gainLossFloat = float(gainLoss[0])
            tickerItem = [TickerList[i], gainLossFloat]
            gainLossList.append(tickerItem)
        except:
            continue

    #Sorts Gain Loss By Coefficient
    gainLossList = BubbleSort(gainLossList)

    # Compares GainLoss to Threshold and creates a return list
    for i in range(len(gainLossList)):
        if i < len(gainLossList) * GainLossThreshold:                    
            # Create a dataset for ticker
            dataSet = CreateDataSetForTicker(gainLossList[i][0])
            
            # Creates the dataframe from data
            df = DataFrameFromData(dataSet)
            Close = df.pop('Close')
            
            # Predicts Models
            predictionPercent = (predictModel.predict(df) / Close[0]) * 100

            # Converts to floats
            predictionPercentFloat = float(predictionPercent)
            tickerItem = [gainLossList[i][0], predictionPercentFloat]
            returnList.append(tickerItem)

    # Sorts Return List
    returnList = BubbleSort(returnList)

    # Prints Return List
    for i in range(len(returnList)):
        print(f"{returnList[i][0]}, {returnList[i][1]}")

    # Returns ReturnList
    return returnList 
        
def GainLossFromTicker(Ticker):
    # Create a dataset for ticker
    dataSet = CreateDataSetForTicker(Ticker)
    
    # Creates the dataframe from data
    df = DataFrameFromData(dataSet)
    Close = df.pop('Close')
    
    # Reshape the dataset
    df = df.to_numpy()
    df_reshaped = df.reshape(df.shape[0],df.shape[1],1)
    
    # Loads TensorFlow Model
    load_model = tf.keras.models.load_model('saved_model/stockTFGainLossModel.h5')
    #load_model.summary()

    # Evaluate the Data
    predictionNumber = load_model.predict(df)
    if load_model.predict(df) > 0.8:
        prediction = 'gain'
    else:
        prediction = 'loss'
    print(f"Prediction: {prediction}, {predictionNumber}")
    return prediction

def PredictFromTicker(Ticker):
    # Create a dataset for ticker
    dataSet = CreateDataSetForTicker(Ticker)
    
    # Creates the dataframe from data
    df = DataFrameFromData(dataSet)
    Close = df.pop('Close')

    # Reshape the dataset
    df = df.to_numpy()
    df_reshaped = df.reshape(df.shape[0],df.shape[1],1)
    
    # Loads TensorFlow Model
    load_model = tf.keras.models.load_model('saved_model/stockTFmodel.h5')
    #load_model.summary()

    # Evaluate the Data
    predictionPercent = (load_model.predict(df) / Close[0]) * 100
    predictionPercent = float(predictionPercent[0])
    print(f"Prediction: {predictionPercent:0.2}%")
    return predictionPercent


def DataFrameFromData(dataSet):    
    # Creates the dataframe from data
    dfData = StringIO(dataSet)
    names = ['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Volume', 'Change', '50 Day MA', '100 Day MA', '200 Day MA','50 Day Support', '100 Day Support', '150 Day Support', '200 Day Support','50 Day Resistance', '100 Day Resistance', '150 Day Resistance', '200 Day Resistance','50 EMA', '100 EMA', '150 EMA', '200 EMA','50 AVG Gain', '100 AVG Gain', '150 AVG Gain', '200 AVG Gain','50 AVG Loss', '100 AVG Loss', '150 AVG Loss', '200 AVG Loss', 'RSI']
    df = pd.read_csv(dfData, names=names)

    # Removes and Stores UnNeeded Data
    dates = df.pop('Date')
    tickers = df.pop('Ticker')
    Open = df.pop('Open')
    High = df.pop('High')
    Low = df.pop('Low')
    # Close = df.pop['Close']
    Volume = df.pop('Volume')
    Change = df.pop('Change')
    
    return df
    
def CreateDataSetForTicker(Ticker):
    tickerName = Ticker 
    startTime = datetime.now()
    printTime = startTime.time()
    row = [None] * 32
    currentDate = startTime
    currentYear = currentDate.strftime("%Y")              
    # Clear Text File Before starting
    endDate = currentDate - timedelta(days=300)
    currentDateString = currentDate.strftime("%m/%d/%Y")
    try:
        # Get Data
        df = yf.Ticker(Ticker).history(start = endDate, end = currentDate)
        frameSize = len(df.index) - 1
        # Setting Preloop Variables
        currentSum = 0
        openValue = float(df["Close"][-2])
        closeValue = float(df["Open"][-2])
        Change = float(df["Close"][-1]) - float(df["Close"][-2])
        ActualChange = float(df["Close"][-1]) - float(df["Close"][-2])
        support = df["Close"][-2]
        resistance = df["Close"][-2]
        smoothing = 2
        avgGain = 0
        avgLoss = 0
        gainCount = 0
        lossCount = 0
        #First Loop - find info needed before other info
        for i in range(frameSize - 1):
            index = -(i + 2)
            # Find Moving Average
            try:
                currentSum += df["Close"][index]
                if i > 0:
                    _200DayMovingAverage = currentSum / i
                if i == 49:
                    _50DayMovingAverage = _200DayMovingAverage
                if i == 99:
                    _100DayMovingAverage = _200DayMovingAverage
            except:
                if i < 49:
                    _50DayMovingAverage = "N/A"
                if i < 99:
                    _100DayMovingAverage = "N/A"
                if i < 199:
                    _200DayMovingAverage = "N/A"
                break                    
        ema = _200DayMovingAverage
        #Main Loop
        for i in range(frameSize - 1):
            Change = float(df["Close"][index]) - float(df["Close"][index + 1])
            #Find Resistance and Support points for periods of time
            if df["Low"][index] < support:
                support = df["Low"][index]
            if df["High"][index] > resistance:
                resistance = df["High"][index]
            if i == 50:
                _50DaySupport = support
                _50DayResistance = resistance
            if i == 100:
                _100DaySupport = support
                _100DayResistance = resistance
            if i == 150:
                _150DaySupport = support
                _150DayResistance = resistance
            if i == 200:
                _200DaySupport = support
                _200DayResistance = resistance
            # Find Exponetial Moving Average
            ema = (df["Close"][index] * (smoothing / (1 + i))) + (ema * (1 - (smoothing / (1 + i))))
            if i == 50: 
                _50DayEma = ema
            if i == 100:
                _100DayEma = ema
            if i == 150:
                _150DayEma = ema
            if i == 200:
                _200DayEma = ema
            # Find Average Gain and Loss
            if Change != 0:
                if Change > 0:
                    gainCount += 1
                    avgGain += Change
                else:
                    lossCount -= 1
                    avgLoss += Change
            if i == 50:
                if avgGain == 0:
                    _50DayAvgGain = 0.00001 # Prevents a devide by 0 error for RSI
                else:
                    _50DayAvgGain = abs(float(avgGain)) / gainCount
                if avgLoss == 0:
                    _50DayAvgLoss = 0.00001 # Prevents a devide by 0 error for RSI
                else:
                    _50DayAvgLoss = abs(float(avgLoss)) / lossCount
            if i == 100:
                if avgGain == 0:
                    _100DayAvgGain = 0.00001 # Prevents a devide by 0 error for RSI
                else:
                    _100DayAvgGain = abs(float(avgGain)) / gainCount
                if avgLoss == 0:
                    _100DayAvgLoss = 0.00001 # Prevents a devide by 0 error for RSI
                else:
                    _100DayAvgLoss = abs(float(avgLoss)) / lossCount
            if i == 150:
                if avgGain == 0:
                    _150DayAvgGain = 0.00001 # Prevents a devide by 0 error for RSI
                else:
                    _150DayAvgGain = abs(float(avgGain)) / gainCount
                if avgLoss == 0:
                    _150DayAvgLoss = 0.00001 # Prevents a devide by 0 error for RSI
                else:
                    _150DayAvgLoss = abs(float(avgLoss)) / lossCount
            if i == 200:
                if avgGain == 0:
                    _200DayAvgGain = 0.00001 # Prevents a devide by 0 error for RSI
                else:
                    _200DayAvgGain = abs(float(avgGain)) / gainCount
                if avgLoss == 0:
                    _200DayAvgLoss = 0.00001 # Prevents a devide by 0 error for RSI
                else:
                    _200DayAvgLoss = abs(float(avgLoss)) / lossCount
        # Find Reletive Strength Index
        RSI = 100 - (100 / (1 + (_50DayAvgGain / _50DayAvgLoss)))
        # Create Row
        row[0] = currentDateString
        row[1] = Ticker
        row[2] = df["Open"][-1]
        row[3] = df["High"][-1]
        row[4] = df["Low"][-1]
        row[5] = df["Close"][-1]
        row[6] = df["Volume"][-1]
        row[7] = ActualChange
        row[8] = float(_50DayMovingAverage) - float(row[5])
        row[9] = float(_100DayMovingAverage) - float(row[5])
        row[10] = float(_200DayMovingAverage) - float(row[5])
        row[11] = float(_50DaySupport) - float(row[5])
        row[12] = float(_100DaySupport) - float(row[5])
        row[13] = float(_150DaySupport) - float(row[5])
        row[14] = float(_200DaySupport) - float(row[5])
        row[15] = float(_50DayResistance) - float(row[5])
        row[16] = float(_100DayResistance) - float(row[5])
        row[17] = float(_150DayResistance) - float(row[5])
        row[18] = float(_200DayResistance) - float(row[5])
        row[19] = float(_50DayEma) - float(row[5])
        row[20] = float(_100DayEma) - float(row[5])
        row[21] = float(_150DayEma) - float(row[5])
        row[22] = float(_200DayEma) - float(row[5])
        row[23] = _50DayAvgGain
        row[24] = _100DayAvgGain
        row[25] = _150DayAvgGain
        row[26] = _200DayAvgGain
        row[27] = _50DayAvgLoss
        row[28] = _100DayAvgLoss
        row[29] = _150DayAvgLoss
        row[30] = _200DayAvgLoss
        row[31] = RSI
        # Turn Row into String
        writeString = f"\n{row[0]},{row[1]},{row[2]:0.2f},{row[3]:0.2f},{row[4]:0.2f},{row[5]:0.2f},{row[6]:0.2f},{row[7]:0.2f},{row[8]:0.2f},{row[9]:0.2f},{row[10]:0.2f},{row[11]:0.2f},{row[12]:0.2f},{row[13]:0.2f},{row[14]:0.2f},{row[15]:0.2f},{row[16]:0.2f},{row[17]:0.2f},{row[18]:0.2f},{row[19]:0.2f},{row[20]:0.2f},{row[21]:0.2f},{row[22]:0.2f},{row[23]:0.2f},{row[24]:0.2f},{row[25]:0.2f},{row[26]:0.2f},{row[27]:0.2f},{row[28]:0.2f},{row[29]:0.2f},{row[30]:0.2f},{row[31]:0.2f}"
        return writeString
    except Exception as e:
        print(f"An Error Occured{e}")


def BubbleSort(SortingList):
    # Bubble Sorting Algorithms to find highest predicted
    for i in range(len(SortingList)):
        for j in range(len(SortingList) - 1):
            if SortingList[j][1] < SortingList[j+1][1]:
                temp = SortingList[j]
                SortingList[j] = SortingList[j+1]
                SortingList[j+1] = temp
    return SortingList


if __name__ == '__main__':
    testList = ['aapl','amzn','btc','gold','hon']
    # GainLossFromTicker('hon')
    # PredictList(testList, 0.1)
    # PredictFromFile('Test100.csv', 0.25)
    # DailyListNasdaq(0.2)
    RetrieveListFromFile("DailyList.csv")
