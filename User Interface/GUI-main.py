import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import ClassAlpaca1

kivy.require('1.050.0')

# Need Buy & Sell functions in all buttons for PosList

# John's GetEquity() function goes here
trader = ClassAlpaca1.AlpacaTrader()
equity = trader.account.cash
buy = trader.postion_size()

# Tickers from Steven's top 5 list goes here
ticker1 = 'A'
ticker2 = 'B'
ticker3 = 'C'
ticker4 = 'D'
ticker5 = 'E'

# Number of Tickers owned from John's API for top 5 tickers goes here
pos1 =  trader.get_positions()
ticker1Owned = pos1
ticker2Owned = 0
ticker3Owned = 0
ticker4Owned = 0
ticker5Owned = 0


class EquityLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.text = str(equity)


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

        tickerVal1 = Label(size_hint_y = .05, text = ticker1)
        ownedVal1 = Label(size_hint_y = .05, text = str(ticker1Owned))
        buyBtn1 = Button(size_hint_y = .05, text = 'Buy')
        sellBtn1 = Button(size_hint_y = .05, text = 'Sell')

        tickerVal2 = Label(size_hint_y = .05, text = ticker2)
        ownedVal2 = Label(size_hint_y = .05, text = str(ticker2Owned))
        buyBtn2 = Button(size_hint_y = .05, text = 'Buy')
        sellBtn2 = Button(size_hint_y = .05, text = 'Sell')

        tickerVal3 = Label(size_hint_y = .05, text = ticker3)
        ownedVal3 = Label(size_hint_y = .05, text = str(ticker3Owned))
        buyBtn3 = Button(size_hint_y = .05, text = 'Buy')
        sellBtn3 = Button(size_hint_y = .05, text = 'Sell')

        tickerVal4 = Label(size_hint_y = .05, text = ticker4)
        ownedVal4 = Label(size_hint_y = .05, text = str(ticker4Owned))
        buyBtn4 = Button(size_hint_y = .05, text = 'Buy')
        sellBtn4 = Button(size_hint_y = .05, text = 'Sell')

        tickerVal5 = Label(size_hint_y = .05, text = ticker5)
        ownedVal5 = Label(size_hint_y = .05, text = str(ticker5Owned))
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
    print(str(trader.get_positions()))

    
