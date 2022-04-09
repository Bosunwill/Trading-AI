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


base_url = "https://paper-api.alpaca.markets"
# base_url = 'https://data.alpaca.markets/v2'

ACCOUNT_URL = "{}/v2/account".format(base_url)
ORDERS_URL = "{}/v2/orders".format(base_url)

API_KEY = 'PKZQ8BRYNILCSQXE5XNH'
SECRET_KEY = 'S8a4bqNLcfiZgk7uoKp4gbPbKYM8a92Cy2z3spMR'

HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url, api_version='v2')

def make_order(lst, qty=1):
    for stock in lst:
        api.submit_order(stock, qty=qty, side='buy', type='market', time_in_force='day')

def make_single_order(stock, qty=1):
    api.submit_order(stock, qty=qty, side='buy', type='market', time_in_force='day')
    
    
stockList = ['APPS','GE','RGF','TSLA']

# Setting parameters before calling method
symbol = "SPY"
timeframe = "1year"
start = "2022-01-01"
end = "2022-04-05"


spy_bars = api.get_bars(symbol, timeframe, start, end).df #datafrane from bars


# Retrieve daily bars for SPY in a dataframe and printing the first 5 rows
print(spy_bars.head())


opn = spy_bars['open']
high=spy_bars['high']
low=spy_bars['low'] 
close=spy_bars['close']

# print(opn)
# print(high)
# print(low)
# print(close)


# single = make_single_order('GOOG',25)
# multi_gets_list = make_order(stockList,25)