####           Program to Jehnerate local files containing data-sets needed for Training          ####
####  Information pulled from yfinance and processed using basic algorithm for market indicators  ####
####          Written by Stephen Jehner for SD202-10546: Advanced Python Machine Learning         ####

import yfinance as yf
import numpy as np
import pandas as pd
import csv
from datetime import datetime, timedelta

# Creates local CSV File containing DataSet
def GenerateFile(tickers, dateRange, startDateTime):
    startTime = datetime.now()
    printTime = startTime.time()
    print(f"Start Time: {printTime}")
    row = [None] * 35
    currentYear = 0
    # Loop through Data and add to file
    for day in range(dateRange):
        prevYear = currentYear
        currentDate = startDateTime - timedelta(days=day)
        currentYear = currentDate.strftime("%Y")
        fileName = f"DataSets\dataSet_{currentYear}.csv" #Creates a new file for each year to break file into bite-sized segments
        # Check if new year and make new file if so
        if currentYear != prevYear:
            # Clear Text File Before starting
            with open(fileName, 'w') as f:
                f.truncate(0)
                f.write(f"Date, Ticker, Open, High, Low, Close, Volume, Change, 50 Day MA, 100 Day MA, 200 Day MA," # Columns 0-10
                        f"50 Day Support, 100 Day Support, 150 Day Support, 200 Day Support," # Columns 11-14
                        f"50 Day Resistance, 100 Day Resistance, 150 Day Resistance, 200 Day Resistance,"  # Columns 15 - 18
                        f"50 EMA, 100 EMA, 150 EMA, 200 EMA," # Columns 19-22
                        f"50 AVG Gain, 100 AVG Gain, 150 AVG Gain, 200 AVG Gain," # Columns 23-26
                        f"50 AVG Loss, 100 AVG Loss, 150 AVG Loss, 200 AVG Loss, RSI," # Columns 27 - 31
                        )  # Columns 32 -
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
                    openValue = float(df["Close"][-1])
                    closeValue = float(df["Close"][-2])
                    Change = openValue - closeValue
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
                        if df["Low"][i] < support:
                            support = df["Low"][-i]
                        if df["High"][i] > resistance:
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
                    # Turn Row into String
                    writeString = f"\n{row[0]},{row[1]},{row[2]:0.2f},{row[3]:0.2f},{row[4]:0.2f},{row[5]:0.2f},{row[6]:0.2f},{row[7]:0.2f},{row[8]:0.2f},{row[9]:0.2f},{row[10]:0.2f},{row[11]:0.2f},{row[12]:0.2f},{row[13]:0.2f},{row[14]:0.2f},{row[15]:0.2f},{row[16]:0.2f},{row[17]:0.2f},{row[18]:0.2f},{row[19]:0.2f},{row[20]:0.2f},{row[21]:0.2f},{row[22]:0.2f},{row[23]:0.2f},{row[24]:0.2f},{row[25]:0.2f},{row[26]:0.2f},{row[27]:0.2f},{row[28]:0.2f},{row[29]:0.2f},{row[30]:0.2f},{row[31]:0.2f}"
                    # Add Row to CSV File
                    written = False
                    # Gives 10 tries to access the file before throwing exception
                    for attempt in range(10):
                        try:
                            with open(fileName, 'a') as f:
                                f.write(writeString)
                        except:
                            print("Error occured when accessing file, trying again")
                            continue
                        else:
                            written = True
                            break
                    # If write was unsuccessfull raises error
                    if written == False:
                        raise Exception("Could Not Write to File")
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
                # Prints the elapsed time to the console
                elapsedTime = datetime.now() - startTime
                tickerLen = len(tickers)
                print(f"Current working date: {currentDate}   -----   Ticker {thisTicker}({tickers[thisTicker]}) of {tickerLen} completed   -----   Elapsed Time: {elapsedTime}")

# Gets Tickers from File
def GetTickers():
    tickers = []
    with open('nasdaq.csv', newline='') as tickerFile:
        reader = csv.reader(tickerFile)
        stockList = list(reader)
        for stock in stockList:
            tickers.append(stock[0])
    return tickers

dateRange = 7300 # Runs for 20 years or until there is not enough information to continue
tickers = GetTickers()

GenerateFile(tickers, dateRange, datetime.now().date())
