# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:54:40 2022

@author: ksbig
"""

import alpaca_trade_api as tradeapi


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

    
    def postion_size(self):
        self.last_price = api.get_latest_trade(self.symbol).price
        target_qty = self.balance *.03 // self.last_price
        self.send_order(target_qty)

    def todays_win_loss(self):
        balance_change = float(self.account.equity) - float(self.account.last_equity)
        return (balance_change)

    def buying_power(self):
        return (self.account.cash)

    def cancel(self):
        api.cancel_all_orders()
        return print('cancelled all orders')

    def basic_order(self,symbol):
        api.submit_order(symbol, qty=1,side='buy', type='market')
        
    def get_position1(self):
        assets = api.list_positions()
        symbols = [asset.symbol for asset in assets]
        return(symbols[0])
         
    def get_position2(self):
       assets = api.list_positions()
       symbols = [asset.symbol for asset in assets]
       return(symbols[-1])

    def get_num_share1(self):
       assets = api.list_positions()
       symbols = [asset.qty for asset in assets]
       return (symbols[0])

    def get_num_share2(self):
       assets = api.list_positions()
       symbols = [asset.qty for asset in assets]
       return (symbols[-1])
        
    def sell_it(self,symbol):
        sell = api.submit_order(symbol,qty=1,side='sell',type='market')

           
if __name__ == '__main__':
    trader = AlpacaTrader()
    # trader.set_symbol_lst(['OILU', 'LXU', 'CRGY', 'BPT', 'CHKEL', 'SGML', 'CHKEZ', 'AMR', 'ZETA', 'NRT', 'IPI', 'NRGV', 'CHKEW', 'AR', 'UAN'])
    trader.basic_order('TSLA')


 

