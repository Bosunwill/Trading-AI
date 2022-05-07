import kivy
import yfinance as yf
from datetime import datetime, timedelta
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

kivy.require('1.050.0')

# Loads the TF related functions
from UserInterface.TFLoadAndFunctions import *

# Loads the Alpaca Class
from AlpacaAPI.ClassAlpaca import *

# Creates a trader object for the alpaca api
trader = AlpacaTrader()

# Need Buy & Sell functions in all buttons for PosList

# John's GetEquity() function goes here
equity = trader.account.equity

# Retrieves top 5 list from 'DailyList.csv'
predictedTickers = RetrieveListFromFile('UserInterface/DailyList.csv')

# Place Tickers into variables
ticker1 = str(predictedTickers[0][0])
ticker2 = str(predictedTickers[1][0])
ticker3 = str(predictedTickers[2][0])
ticker4 = str(predictedTickers[3][0])
ticker5 = str(predictedTickers[4][0])

ticker1Price = f"${yf.Ticker(ticker1).history()['Close'].iloc[-1]:0.2f}"
ticker2Price = f"${yf.Ticker(ticker2).history()['Close'].iloc[-1]:0.2f}"
ticker3Price = f"${yf.Ticker(ticker3).history()['Close'].iloc[-1]:0.2f}"
ticker4Price = f"${yf.Ticker(ticker4).history()['Close'].iloc[-1]:0.2f}"
ticker5Price = f"${yf.Ticker(ticker5).history()['Close'].iloc[-1]:0.2f}"


ticker1Score = float(predictedTickers[0][1])
ticker2Score = float(predictedTickers[1][1])
ticker3Score = float(predictedTickers[2][1])
ticker4Score = float(predictedTickers[3][1])
ticker5Score = float(predictedTickers[4][1])

# Number of Tickers owned from John's API for top 5 tickers goes here
tickerOwnedList = trader.get_positions()

ticker1Owned = tickerOwnedList[0].symbol if len(tickerOwnedList) > 0 else "N/A"
ticker2Owned = tickerOwnedList[1].symbol if len(tickerOwnedList) > 1 else "N/A"
ticker3Owned = tickerOwnedList[2].symbol if len(tickerOwnedList) > 2 else "N/A"
ticker4Owned = tickerOwnedList[3].symbol if len(tickerOwnedList) > 3 else "N/A"
ticker5Owned = tickerOwnedList[4].symbol if len(tickerOwnedList) > 4 else "N/A"

qty1Owned = tickerOwnedList[0].qty if len(tickerOwnedList) > 0 else "N/A"
qty2Owned = tickerOwnedList[1].qty if len(tickerOwnedList) > 1 else "N/A"
qty3Owned = tickerOwnedList[2].qty if len(tickerOwnedList) > 2 else "N/A"
qty4Owned = tickerOwnedList[3].qty if len(tickerOwnedList) > 3 else "N/A"
qty5Owned = tickerOwnedList[4].qty if len(tickerOwnedList) > 4 else "N/A"


class EquityLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = f"$ {equity}"


class PosListLabel(Label):
    pass

class GraphImage(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # image of graph goes here, use top 5 stocks list from Steven

        pass


class TopStocksGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        tickerLbl = Label(size_hint_y = .05, text = 'Ticker')
        priceLbl = Label(size_hint_y = .05, text = 'Price')
        scoreLbl = Label(size_hint_y = .05, text = 'Score')
        self.add_widget(tickerLbl)
        self.add_widget(priceLbl)
        self.add_widget(scoreLbl)

        tickerVal1 = Label(size_hint_y = .05, text = ticker1)
        priceVal1 = Label(size_hint_y = .05, text = ticker1Price)
        scoreVal1 = Label(size_hint_y = .05, text = f"{ticker1Score:0.2f}")
        self.add_widget(tickerVal1)
        self.add_widget(priceVal1)
        self.add_widget(scoreVal1)

        tickerVal2 = Label(size_hint_y = .05, text = ticker2)
        priceVal2 = Label(size_hint_y = .05, text = ticker2Price)
        scoreVal2 = Label(size_hint_y = .05, text = f"{ticker2Score:0.2f}")
        self.add_widget(tickerVal2)
        self.add_widget(priceVal2)
        self.add_widget(scoreVal2)

        tickerVal3 = Label(size_hint_y = .05, text = ticker3)
        priceVal3 = Label(size_hint_y = .05, text = ticker3Price)
        scoreVal3 = Label(size_hint_y = .05, text = f"{ticker3Score:0.2f}")
        self.add_widget(tickerVal3)
        self.add_widget(priceVal3)
        self.add_widget(scoreVal3)

        tickerVal4 = Label(size_hint_y = .05, text = ticker4)
        priceVal4 = Label(size_hint_y = .05, text = ticker4Price)
        scoreVal4 = Label(size_hint_y = .05, text = f"{ticker4Score:0.2f}")
        self.add_widget(tickerVal4)
        self.add_widget(priceVal4)
        self.add_widget(scoreVal4)

        tickerVal5 = Label(size_hint_y = .05, text = ticker5)
        priceVal5 = Label(size_hint_y = .05, text = ticker5Price)
        scoreVal5 = Label(size_hint_y = .05, text = f"{ticker5Score:0.2f}")
        self.add_widget(tickerVal5)
        self.add_widget(priceVal5)
        self.add_widget(scoreVal5)
  

class GraphChartGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    

class PosGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        tickerLbl = Label(size_hint_y = .05, text = 'Ticker')
        ownedLbl = Label(size_hint_y = .05, text = '# Owned')
        fillLbl = Label(size_hint_y = .05, text = ' ')
        fillLbl2 = Label(size_hint_y = .05, text = ' ')

        tickerVal1 = Label(size_hint_y = .05, text = ticker1Owned)
        ownedVal1 = Label(size_hint_y = .05, text = str(qty1Owned))
        buyBtn1 = Button(size_hint_y = .05, text = 'Buy')
        sellBtn1 = Button(size_hint_y = .05, text = 'Sell')

        tickerVal2 = Label(size_hint_y = .05, text = ticker2Owned)
        ownedVal2 = Label(size_hint_y = .05, text = str(qty2Owned))
        buyBtn2 = Button(size_hint_y = .05, text = 'Buy')
        sellBtn2 = Button(size_hint_y = .05, text = 'Sell')

        tickerVal3 = Label(size_hint_y = .05, text = ticker3Owned)
        ownedVal3 = Label(size_hint_y = .05, text = str(qty3Owned))
        buyBtn3 = Button(size_hint_y = .05, text = 'Buy')
        sellBtn3 = Button(size_hint_y = .05, text = 'Sell')

        tickerVal4 = Label(size_hint_y = .05, text = ticker4Owned)
        ownedVal4 = Label(size_hint_y = .05, text = str(qty4Owned))
        buyBtn4 = Button(size_hint_y = .05, text = 'Buy')
        sellBtn4 = Button(size_hint_y = .05, text = 'Sell')

        tickerVal5 = Label(size_hint_y = .05, text = ticker5Owned)
        ownedVal5 = Label(size_hint_y = .05, text = str(qty5Owned))
        buyBtn5 = Button(size_hint_y = .05, text = 'Buy')
        sellBtn5 = Button(size_hint_y = .05, text = 'Sell')

        self.add_widget(tickerLbl)
        self.add_widget(ownedLbl)
        self.add_widget(fillLbl)
        self.add_widget(fillLbl2)

        self.add_widget(tickerVal1)
        self.add_widget(ownedVal1)
        self.add_widget(buyBtn1)
        self.add_widget(sellBtn1)

        self.add_widget(tickerVal2)
        self.add_widget(ownedVal2)
        self.add_widget(buyBtn2)
        self.add_widget(sellBtn2)

        self.add_widget(tickerVal3)
        self.add_widget(ownedVal3)
        self.add_widget(buyBtn3)
        self.add_widget(sellBtn3)

        self.add_widget(tickerVal4)
        self.add_widget(ownedVal4)
        self.add_widget(buyBtn4)
        self.add_widget(sellBtn4)

        self.add_widget(tickerVal5)
        self.add_widget(ownedVal5)
        self.add_widget(buyBtn5)
        self.add_widget(sellBtn5)

        fillLblEnd = Label(text = ' ')
        self.add_widget(fillLblEnd)

class MultipleLayout(GridLayout):
    pass

class TradingAI(App):
    def build(self):
        return MultipleLayout()

if __name__ == '__main__':
    TradingAI().run()
