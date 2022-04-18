# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:54:40 2022

@author: ksbig
"""

import alpaca_trade_api as tradeapi
import pandas as pd
import matplotlib.pyplot as plt
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit
import plotly.express as px
import plotly.graph_objects as go

base_url = "https://paper-api.alpaca.markets"
# base_url = 'https://data.alpaca.markets/v2'

ACCOUNT_URL = "{}/v2/account".format(base_url)
ORDERS_URL = "{}/v2/orders".format(base_url)

API_KEY = 'PKZQ8BRYNILCSQXE5XNH'
SECRET_KEY = 'S8a4bqNLcfiZgk7uoKp4gbPbKYM8a92Cy2z3spMR'

HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url, api_version='v2')
account = api.get_account()


def make_order_basic(lst, qty=1):
    for stock in lst:
        api.submit_order(stock, qty=qty, side='buy', type='market', time_in_force='day')

def make_single_order(stock, qty=1):
    api.submit_order(stock, qty=qty, side='buy', type='market', time_in_force='day')


def make_03_position_order(sym):
    last_price= api.get_latest_trade(sym).price
    bal = float(account.last_equity)
    print(bal)
    qty = bal *.03 // last_price
    position = int(api.get_position(sym).qty)
     
    api.submit_order(sym, qty, side='buy', type='market', time_in_force='day')
    print(f"Balance was {bal} and you just placed a BUY order for {qty} shares of {sym}")

    # return print(api.list_orders(status='open', limit=1, nested=True))


def plot_sym(sym):
    candlestick_fig = go.Figure(data=[go.Candlestick(x=sym.index,
                                                     open=sym['open'],
                                                     high=sym['high'],
                                                     low=sym['low'],
                                                     close=sym['close'])])
    candlestick_fig.update_layout(
        title="Candlestick chart for {0}".format(sym),
        xaxis_title=start + ' ' + end,
        yaxis_title="Price {0}".format(api.get_bars(sym, timeframe)))
    candlestick_fig.show()
    
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

x = api.get_bars(symbol, timeframe, start, end).df
plot_sym(x)