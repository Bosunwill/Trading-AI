# -*- coding: utf-8 -*-
import alpaca_trade_api as tradeapi


base_url = "https://paper-api.alpaca.markets"
# base_url = 'https://data.alpaca.markets/v2'

ACCOUNT_URL = "{}/v2/account".format(base_url)
ORDERS_URL = "{}/v2/orders".format(base_url)

API_KEY = 'PKZQ8BRYNILCSQXE5XNH'  # ask Jared about encryption of these
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
        

        # The connection to the Alpaca API
        self.api = tradeapi.REST(
            self.key_id,
            self.secret_key,
            self.base_url
        )

        try:
            self.balance = float(self.account.last_equity)
        except:
            self.balance = 0.00

    def get_my_order_id(self):
        return print(self.my_order_id)

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return print(self.symbol)

    def set_symbol_lst(self, symbol_lst):
        self.symbol_lst = symbol_lst

    def get_symbol_lst(self):
        return print(self.symbol_lst)

    def todays_win_loss(self):
        balance_change = float(self.account.equity) - \
            float(self.account.last_equity)
        print(f'Today\'s portfolio balance change: ${balance_change}')

    def buying_power(self):
        return print(self.account.cash)
        # return print(f'${self.account.buying_power} via margin and ${self.account.cash} is cash.')

    def get_positions(self):
        return api.list_positions()


if __name__ == '__main__':
    trader = AlpacaTrader()
    # trader.set_symbol_lst(['OILU', 'LXU', 'CRGY', 'BPT', 'CHKEL', 'SGML', 'CHKEZ', 'AMR', 'ZETA', 'NRT', 'IPI', 'NRGV', 'CHKEW', 'AR', 'UAN'])

