import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout

kivy.require('1.10.0')

class MultipleLayout(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class TradingAI(App):
    def build(self):
        return MultipleLayout()
        

if __name__ == '__main__':
    TradingAI().run()
