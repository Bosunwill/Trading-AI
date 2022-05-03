import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

kivy.require('1.10.0')

class EquityLabel(Label):
    pass

class PosListLabel(Label):
    pass

class GraphImage(Button):
    pass

class TopStocksGrid(GridLayout):
    pass

class PosGrid(GridLayout):
    pass

class MultipleLayout(GridLayout):
    pass

class TradingAI(App):
    def build(self):
        return MultipleLayout()

if __name__ == '__main__':
    TradingAI().run()
