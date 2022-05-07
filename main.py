import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from UserInterface.ClassAlpaca1 import AlpacaTrader

kivy.require('1.050.0')

trader = AlpacaTrader()

winLoss = "Today's Gain/Loss: " + str(int(trader.todays_win_loss()))

# Changing to static list of tickers to simplify for completion
ticker1 = 'AAPL'
ticker2 = 'AMZN'
ticker3 = 'GE'
ticker4 = 'BAC'
ticker5 = 'AMD'

# Changing to api call for single ticker position quantity to simplify for completion
ticker1Owned = 0
ticker2Owned = 0
ticker3Owned = 0
ticker4Owned = 0
ticker5Owned = 0

# Need Gain/Loss predictions from Steven
ticker1Pred = 0
ticker2Pred = 0
ticker3Pred = 0
ticker4Pred = 0
ticker5Pred = 0

# action for buy buttons
def buyBtn(tickerBuy):
    trader.basic_order(tickerBuy)

# action for sell buttons
def sellBtn(tickerSell):
    trader.sell_it(tickerSell)

# creates label for current Win/Loss
class WinLossLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.text = str(winLoss)

# creates static label for PosList 
class PosListLabel(Label):
    pass

# creates button with image of chart
class GraphImage(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # image of graph goes here, use top 5 stocks list from Steven

        pass

# Creates Grid which contains Ticker, Price, & Predictions
class TopStocksGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        tickerLbl = Label(size_hint_y = .05, text = 'Ticker')
        priceLbl = Label(size_hint_y = .05, text = 'Price')
        scoreLbl = Label(size_hint_y = .05, text = 'Predicted Gain/Loss')
        self.add_widget(tickerLbl)
        self.add_widget(priceLbl)
        self.add_widget(scoreLbl)

        tickerVal1 = Label(size_hint_y = .05, text = ticker1)
        priceVal1 = Label(size_hint_y = .05, text = '0')
        scoreVal1 = Label(size_hint_y = .05, text = '0')
        self.add_widget(tickerVal1)
        self.add_widget(priceVal1)
        self.add_widget(scoreVal1)

        tickerVal2 = Label(size_hint_y = .05, text = ticker2)
        priceVal2 = Label(size_hint_y = .05, text = '0')
        scoreVal2 = Label(size_hint_y = .05, text = '0')
        self.add_widget(tickerVal2)
        self.add_widget(priceVal2)
        self.add_widget(scoreVal2)

        tickerVal3 = Label(size_hint_y = .05, text = ticker3)
        priceVal3 = Label(size_hint_y = .05, text = '0')
        scoreVal3 = Label(size_hint_y = .05, text = '0')
        self.add_widget(tickerVal3)
        self.add_widget(priceVal3)
        self.add_widget(scoreVal3)

        tickerVal4 = Label(size_hint_y = .05, text = ticker4)
        priceVal4 = Label(size_hint_y = .05, text = '0')
        scoreVal4 = Label(size_hint_y = .05, text = '0')
        self.add_widget(tickerVal4)
        self.add_widget(priceVal4)
        self.add_widget(scoreVal4)

        tickerVal5 = Label(size_hint_y = .05, text = ticker5)
        priceVal5 = Label(size_hint_y = .05, text = '0')
        scoreVal5 = Label(size_hint_y = .05, text = '0')
        self.add_widget(tickerVal5)
        self.add_widget(priceVal5)
        self.add_widget(scoreVal5)
  
# Creates Grid for containing Graph & Chart
class GraphChartGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

# Creates Grid for Tickers owned with buy & sell buttons
class PosGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        tickerLbl = Label(size_hint_y = .05, text = 'Ticker')
        ownedLbl = Label(size_hint_y = .05, text = '# Owned')
        fillLbl = Label(size_hint_y = .05, text = ' ')
        fillLbl2 = Label(size_hint_y = .05, text = ' ')

        tickerVal1 = Label(size_hint_y = .05, text = ticker1)
        ownedVal1 = Label(size_hint_y = .05, text = str(ticker1Owned))
        buyBtn1 = Button(size_hint_y = .05, text = 'Buy')
        buyBtn1.bind(on_press = buyBtn(tickerVal1))
        sellBtn1 = Button(size_hint_y = .05, text = 'Sell')
        sellBtn2.bind(on_press = sellBtn(tickerVal2))

        tickerVal2 = Label(size_hint_y = .05, text = ticker2)
        ownedVal2 = Label(size_hint_y = .05, text = str(ticker2Owned))
        buyBtn2 = Button(size_hint_y = .05, text = 'Buy')
        buyBtn2.bind(on_press = buyBtn(tickerVal2))
        sellBtn2 = Button(size_hint_y = .05, text = 'Sell')
        sellBtn2.bind(on_press = sellBtn(tickerVal2))

        tickerVal3 = Label(size_hint_y = .05, text = ticker3)
        ownedVal3 = Label(size_hint_y = .05, text = str(ticker3Owned))
        buyBtn3 = Button(size_hint_y = .05, text = 'Buy')
        buyBtn3.bind(on_press = buyBtn(tickerVal3))
        sellBtn3 = Button(size_hint_y = .05, text = 'Sell')
        sellBtn3.bind(on_press = sellBtn(tickerVal3))

        tickerVal4 = Label(size_hint_y = .05, text = ticker4)
        ownedVal4 = Label(size_hint_y = .05, text = str(ticker4Owned))
        buyBtn4 = Button(size_hint_y = .05, text = 'Buy')
        buyBtn4.bind(on_press = buyBtn(tickerVal4))
        sellBtn4 = Button(size_hint_y = .05, text = 'Sell')
        sellBtn4.bind(on_press = sellBtn(tickerVal4))

        tickerVal5 = Label(size_hint_y = .05, text = ticker5)
        ownedVal5 = Label(size_hint_y = .05, text = str(ticker5Owned))
        buyBtn5 = Button(size_hint_y = .05, text = 'Buy')
        buyBtn5.bind(on_press = buyBtn(tickerVal5))
        sellBtn5 = Button(size_hint_y = .05, text = 'Sell')
        sellBtn5.bind(on_press = sellBtn(tickerVal5))

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

# Creates master Grid to contain all other items
class MultipleLayout(GridLayout):
    pass

# Create the App to return the Layout
class TradingAI(App):
    def build(self):
        return MultipleLayout()

if __name__ == '__main__':
    TradingAI().run()
