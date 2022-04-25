import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config

kivy.require('1.10.0')

Config.set('graphics', 'resizable', True)

class TradingAI(App):
    def build(self):
        Gl = GridLayout()
        Fl = FloatLayout()
        lblStockList = Label(text = 'Stock List', size_hint = (.1,.05), pos_hint = {'x':.1, 'y':.9})
        Fl.add_widget(lblStockList)
        lblWatchList = Label(text = 'My Watch List', size_hint = (.1, .05), pos_hint={'x': .8, 'y': .9})
        Fl.add_widget(lblWatchList)


        lblTickerTitle = Label(text = 'Ticker', size_hint = (.1, .05), pos_hint = {'x': .3, 'y': .925})
        Fl.add_widget(lblTickerTitle)
        lblPriceTitle = Label(text = 'Price', size_hint = (.1, .05), pos_hint = {'x': .4, 'y': .925})
        Fl.add_widget(lblPriceTitle)
        lblScoreTitle = Label(text = 'Score', size_hint = (.1, .05), pos_hint = {'x': .5, 'y': .925})
        Fl.add_widget(lblScoreTitle)
        lblBuySellTitle = Label(text = 'Buy/Sell', size_hint = (.1, .05), pos_hint = {'x': .6, 'y': .925})
        Fl.add_widget(lblBuySellTitle)

        lblTickerListTitle = Label(text = 'Ticker', size_hint = (.1, .05), pos_hint = {'x': .3, 'y': .4})
        Fl.add_widget(lblTickerListTitle)
        lblPriceListTitle = Label(text = 'Price', size_hint = (.1, .05), pos_hint = {'x': .4, 'y': .4})
        Fl.add_widget(lblPriceListTitle)
        lblScoreListTitle = Label(text = 'Score', size_hint = (.1, .05), pos_hint = {'x': .5, 'y': .4})
        Fl.add_widget(lblScoreListTitle)
        lblBuySellListTitle = Label(text = 'Buy/Sell', size_hint = (.1, .05), pos_hint = {'x': .6, 'y': .4})
        Fl.add_widget(lblBuySellListTitle)

        itemTicker = 10;
        itemPrice = 10;
        itemScore = 10;
        itemBuySell = 'Buy';

        lblTicker = Label(text = str(itemTicker), size_hint = (.1, .05), pos_hint = {'x': .3, 'y': .875})
        Fl.add_widget(lblTicker)
        lblPrice = Label(text = str(itemPrice), size_hint = (.1, .05), pos_hint = {'x': .4, 'y': .875})
        Fl.add_widget(lblPrice)
        lblScore = Label(text = str(itemScore), size_hint = (.1, .05), pos_hint = {'x': .5, 'y': .875})
        Fl.add_widget(lblScore)
        lblBuySell = Label(text = itemBuySell, size_hint = (.1, .05), pos_hint = {'x': .6, 'y': .875})
        Fl.add_widget(lblBuySell)


        btnAddStock = Button(text = 'Add Stock', size_hint = (.13, .05), background_color = (.1, .2, .7), pos_hint = {'x':.72, 'y':.1})
        Fl.add_widget(btnAddStock)
        btnRemoveStock = Button(text = 'Remove Stock', size_hint = (.13, .05), background_color = (.1, .2, .7), pos_hint = {'x':.86, 'y':.1})
        Fl.add_widget(btnRemoveStock)

        return Fl

if __name__ == '__main__':
    TradingAI().run()
