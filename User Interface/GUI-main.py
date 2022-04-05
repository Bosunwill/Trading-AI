import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.config import Config

kivy.require('1.10.0')

Config.set('graphics', 'resizable', True)

class TradingAI(App):
    def build(self):
        Fl = FloatLayout()
        btn = Button(text = 'Hello world', size_hint = (.3, .5), background_color = (.1, .4, .5), pos_hint = {'x':.2, 'y':.2})
        Fl.add_widget(btn)
        return Fl

if __name__ == '__main__':
    TradingAI().run()
