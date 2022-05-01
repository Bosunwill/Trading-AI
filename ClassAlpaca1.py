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

API_KEY = 'PKZQ8BRYNILCSQXE5XNH'   #ask Jared about encryption of these
SECRET_KEY = 'S8a4bqNLcfiZgk7uoKp4gbPbKYM8a92Cy2z3spMR'

HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url, api_version='v2')
account = api.get_account()


class AlpacaTrader(object):
    def __init__(self):
        # API authentication keys can be taken from the Alpaca dashboard.
        # https://app.alpaca.markets/paper/dashboard/overview
        self.key_id = API_KEY
        self.secret_key = SECRET_KEY
        self.base_url = 'https://paper-api.alpaca.markets'
        self.account = api.get_account()

        # The symbol(s) we will be trading 
        self.symbol = 'TSLA'
        self.symbol_lst = []

        # When this variable is not None, we have an order open
        # self.current_order = None

        # The closing price of the last aggregate we saw
        # self.last_price = api.get_latest_trade(self.symbol).price

        # The connection to the Alpaca API
        self.api = tradeapi.REST(
            self.key_id,
            self.secret_key,
            self.base_url
        )
   # Get our starting position, in case we already have one open
        try:
            self.position = int(self.api.get_position(self.symbol).qty)
        except:
            # No position exists
            self.position = 0

        try:
            self.balance = float(self.account.last_equity)
        except:
            self.balance = 0.00
            

    def set_symbol(self,symbol):
        self.symbol = symbol

    def get_symbol(self):
        return print(self.symbol)

    def set_symbol_lst(self,symbol_lst):
        self.symbol_lst = symbol_lst

    def get_symbol_lst(self):
        return print(self.symbol_lst)           

    def nasdaq(self):
        active_assets = api.list_assets(status='active')
        # Filter the assets down to just those on NASDAQ.
        nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']
        print(nasdaq_assets)

    def is_tradeable(self):
       
        try:
            for sym in self.symbol_lst:
                try:
                    asset = api.get_asset(sym)
                
                    if asset.tradable == True:
                        print(f'We can trade {sym}.')
                except:
                    pass

        except:
            print('error')
          

    def send_order(self, target_qty):
        if self.position == 0:
            api.submit_order(self.symbol, target_qty, side='buy', type='limit', time_in_force='gtc', limit_price=(int(self.last_price - self.last_price * .10)))
            return print (f'made order {target_qty} of {self.symbol} at {int(self.last_price - self.last_price * .10)}')
         
    def postion_size(self):
        self.last_price = api.get_latest_trade(self.symbol).price
        target_qty = self.balance *.03 // self.last_price
        self.send_order(target_qty)

    def todays_win_loss(self):
        balance_change = float(self.account.equity) - float(self.account.last_equity)
        print(f'Today\'s portfolio balance change: ${balance_change}')  

    def buying_power(self):
        return print(f'${self.account.buying_power} via margin and ${self.account.cash} is cash.')   

    # def plot_sym(sym):
    #     candlestick_fig = go.Figure(data=[go.Candlestick(x=sym.index,
    #                                                     open=sym['open'],
    #                                                     high=sym['high'],
    #                                                     low=sym['low'],
    #                                                     close=sym['close'])])
    #     candlestick_fig.update_layout(
    #         title="Candlestick chart for {0}".format(sym),
    #         xaxis_title=start + ' ' + end,
    #         yaxis_title="Price {0}".format(api.get_bars(sym, timeframe)))
    #     candlestick_fig.show()
           
if __name__ == '__main__':
    trader = AlpacaTrader()
    trader.set_symbol('APPS')
    trader.set_symbol_lst(['OILU', 'LXU', 'CRGY', 'BPT', 'CHKEL', 'SGML', 'CHKEZ', 'AMR', 'ZETA', 'NRT', 'IPI', 'NRGV', 'CHKEW', 'AR', 'UAN'])
 
    # trader.get_symbol()
  
    # trader.postion_size()
    # trader.todays_win_loss()
    # trader.buying_power()
    # trader.nasdaq()
    trader.get_symbol_lst()
    trader.is_tradeable()