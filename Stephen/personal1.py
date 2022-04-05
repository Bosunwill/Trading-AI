# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:53:20 2022

@author: ksbig
"""
import plotly.express as px
import plotly.graph_objects as go
import talib as ta
import re
from alpaca_trade_api.rest import REST, TimeFrame
import alpaca_trade_api as tradeapi
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

base_url = "https://paper-api.alpaca.markets"
# base_url = 'https://data.alpaca.markets/v2'

ACCOUNT_URL = "{}/v2/account".format(base_url)
ORDERS_URL = "{}/v2/orders".format(base_url)

API_KEY = 'PKCUQOO80RTR4BF6B6RX'
SECRET_KEY = 'qV55hQoLLxWJhuXWumO9E8v1pTsR5bKKidrMncbZ'

HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url, api_version='v2')

URL = "https://www.eseykota.com/TT/PHP_TT/TT_charts/stocks/myList.txt"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')
raw = soup.prettify()
tag = (str(soup.encode_contents()))

r = re.compile('[A-Z]')
special_char = '@_!#$%^&*()<>?/\|}{~:;.[]rn'

modSyms = []

for w in tag.split('\\n'):
    modSyms.append(w)

modSyms = list(filter(r.match, modSyms))

cleanSyms = [''.join(x for x in string if not x in special_char)
             for string in modSyms]

strong = [x for x in cleanSyms[0:15]]
strongDf = pd.DataFrame(strong, columns=['strong'])
strongCsv = strongDf.to_csv('strong.csv', 'a', index=True)

weak = [x for x in cleanSyms[15:]]
weakDf = pd.DataFrame(weak, columns=['weak'])
weakCsv = weakDf.to_csv('weak.csv', 'a', index=True)


def add_days_strong(lst):
    for stock in lst:
        strongDf.loc[len(strongDf)] = stock


def add_days_weak(lst):
    for stock in lst:
        weakDf.loc[len(weakDf)] = stock


def get_data_strong(lst):
    for stock in lst:
        with open('alpacaStrong.csv', 'a', newline='') as file:
            theWriter = csv.writer(file)
            theWriter.writerow(api.get_bars(lst, TimeFrame.Day))


def get_data_weak(lst):
    for stock in lst:
        with open('alpacaWeak.csv', 'a', newline='') as file:
            theWriter = csv.writer(file)
            theWriter.writerow(api.get_bars(lst, TimeFrame.Day))


def make_order(lst, qty=1):
    for stock in lst:
        api.submit_order(stock, qty=qty, side='buy', type='market', time_in_force='day')


def cancel_orders():
    api.cancel_all_orders()


def cancel_specific_order(num):  # ORDER ID Number
    api.cancel_order(num)


def plot_sym(sym):
    candlestick_fig = go.Figure(data=[go.Candlestick(x=sym.index,
                                                     open=sym['open'],
                                                     high=sym['high'],
                                                     low=sym['low'],
                                                     close=sym['close'])])
    candlestick_fig.update_layout(
        title="Candlestick chart for $SPY",
        xaxis_title="Date",
        yaxis_title="Price ($USD)")
    candlestick_fig.show()


sym = 'apps'
timeframe = '1Hour'
start = '2022-01-01'
end = '2022-03-31'

x = api.get_bars(sym, timeframe, start, end).df
plot_sym(x)
print(strongDf)

add_days_strong(strong)
add_days_weak(weak)

print(weakDf)
print(strongDf)
# buy = make_order(strong,25)


# jx=cancel_orders()


# dataTest = get_data_strong(strong)
# dataTest = get_data_weak(weak)

