# Import needed libraries
import os
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import pickle
import yfinance as yf
from datetime import datetime, timedelta

# Creates local CSV File containing DataSet
def GenerateDailyData():
    Rows = []
    tickers = GetTickers()
    row = [None] * 32
    currentDate = datetime.now()
    currentYear = currentDate.strftime("%Y")
    endDate = currentDate - timedelta(days=300)
    currentDateString = currentDate.strftime("%m/%d/%Y")
    if len(tickers) > 0:
        for thisTicker in range(len(tickers)):
            try:
                # Get Data
                df = yf.Ticker(tickers[thisTicker]).history(start = endDate, end = currentDate)
                frameSize = len(df.index) - 1
                # Setting Preloop Variables
                currentSum = 0
                openValue = float(df["Open"][-1])
                closeValue = float(df["Close"][-1])
                Change = float(df["Close"][-1]) - float(df["Close"][-2])
                support = df["Close"][-1]
                resistance = df["Close"][-1]
                smoothing = 2
                avgGain = 0
                avgLoss = 0
                gainCount = 0
                lossCount = 0
                #First Loop - find info needed before other info
                for i in range(frameSize - 1):
                    # Find Moving Average
                    try:
                        currentSum += df["Close"][-i]
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
                    #Find Resistance and Support points for periods of time
                    if df["Low"][-i] < support:
                        support = df["Low"][-i]
                    if df["High"][-i] > resistance:
                        resistance = df["High"][-i]
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
                    ema = (df["Close"][-i] * (smoothing / (1 + i))) + (ema * (1 - (smoothing / (1 + i))))
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
                row[1] = tickers[thisTicker]
                row[2] = df["Open"][-1]
                row[3] = df["High"][-1]
                row[4] = df["Low"][-1]
                row[5] = df["Close"][-1]
                row[6] = df["Volume"][-1]
                row[7] = Change
                row[8] = _50DayMovingAverage
                row[9] = _100DayMovingAverage
                row[10] = _200DayMovingAverage
                row[11] = _50DaySupport
                row[12] = _100DaySupport
                row[13] = _150DaySupport
                row[14] = _200DaySupport
                row[15] = _50DayResistance
                row[16] = _100DayResistance
                row[17] = _150DayResistance
                row[18] = _200DayResistance
                row[19] = _50DayEma
                row[20] = _100DayEma
                row[21] = _150DayEma
                row[22] = _200DayEma
                row[23] = _50DayAvgGain
                row[24] = _100DayAvgGain
                row[25] = _150DayAvgGain
                row[26] = _200DayAvgGain
                row[27] = _50DayAvgLoss
                row[28] = _100DayAvgLoss
                row[29] = _150DayAvgLoss
                row[30] = _200DayAvgLoss
                row[31] = RSI
                # Add Row to rows
                if None in row:
                    continue
                Rows.append(row)
                row = [None] * 32
            except Exception as e:
                # On Error Removes Ticker From List
                try:
                    print(f"{e}\nTicker {tickers[thisTicker]} deleted from list")
                    del tickers[thisTicker]
                    tickerLen = len(tickers)
                    print(f"Current Ticker List Length: {tickerLen}")
                    continue
                except:
                    # This is most likely raised when tickers are deleted and the loop moves out of range of tickers list
                    print("Error Occured, Moving On")
                    break
    return Rows

# Gets Tickers from File
def GetTickers():
    tickers = []
    with open('nasdaq.csv', newline='') as tickerFile:
        reader = csv.reader(tickerFile)
        stockList = list(reader)
        for stock in stockList:
            tickers.append(stock[0])
    return tickers


# Creates the dataframe for training
names = ['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Volume', 'Change', '50 Day MA', '100 Day MA', '200 Day MA','50 Day Support', '100 Day Support', '150 Day Support', '200 Day Support','50 Day Resistance', '100 Day Resistance', '150 Day Resistance', '200 Day Resistance','50 EMA', '100 EMA', '150 EMA', '200 EMA','50 AVG Gain', '100 AVG Gain', '150 AVG Gain', '200 AVG Gain','50 AVG Loss', '100 AVG Loss', '150 AVG Loss', '200 AVG Loss', 'RSI']
df = pd.DataFrame(GenerateDailyData(), columns = names)
print (df)
print (df.shape)

# Create array to run on model
X = np.asarray(df[['50 Day MA', '100 Day MA', '200 Day MA','50 Day Support', '100 Day Support', '150 Day Support', '200 Day Support','50 Day Resistance', '100 Day Resistance', '150 Day Resistance', '200 Day Resistance', '50 EMA', '100 EMA', '150 EMA', '200 EMA','50 AVG Gain', '100 AVG Gain', '150 AVG Gain', '200 AVG Gain','50 AVG Loss', '100 AVG Loss', '150 AVG Loss', '200 AVG Loss', 'RSI']])
tickers = np.asarray(df['Ticker'])

# Loads Pre-Created Model
loadedModel = pickle.load(open("finalizedModel.sav", 'rb'))

# Apply Pro-Created Model
predictions = loadedModel.predict(X)

# Creates list of Predictions and Tickers for sorting
tickerPredictList = []
for i in range(len(predictions)):
    currentItem = [predictions[i], tickers[i]]
    tickerPredictList.append(currentItem);
    
# Bubble Sorting Algorithms to find highest predicted
for i in range(len(tickerPredictList)):
    for j in range(len(tickerPredictList) - 1):
        if tickerPredictList[j][0] < tickerPredictList[j+1][0]:
            temp = tickerPredictList[j]
            tickerPredictList[j] = tickerPredictList[j+1]
            tickerPredictList[j+1] = temp

# Print Results
for i in range(len(tickerPredictList)):
    print(f"Ticker: {tickerPredictList[i][1]}  --  Predicted Change: {tickerPredictList[i][0]:0.2f}")
