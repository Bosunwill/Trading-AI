# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:54:40 2022

@author: ksbig
"""

import alpaca_trade_api as tradeapi
import pandas as pd
#import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
# import pyotp
from pmdarima import auto_arima
import warnings


base_url = "https://paper-api.alpaca.markets"
# base_url = 'https://data.alpaca.markets/v2'

ACCOUNT_URL = "{}/v2/account".format(base_url)
ORDERS_URL = "{}/v2/orders".format(base_url)

API_KEY = 'PKZQ8BRYNILCSQXE5XNH'
SECRET_KEY = 'S8a4bqNLcfiZgk7uoKp4gbPbKYM8a92Cy2z3spMR'

HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url, api_version='v2')

warnings.filterwarnings("ignore")



# Setting parameters before calling method
symbol = "SPY"
timeframe = "1Day"
start = "2022-01-01"
end = "2022-04-05"
# Retrieve daily bars for SPY in a dataframe and printing the first 5 rows


spy_bars = api.get_bars(symbol, timeframe, start, end).df

opn = spy_bars['open']

high=spy_bars['high']

low=spy_bars['low']
               
close=spy_bars['close']


print(high,low)