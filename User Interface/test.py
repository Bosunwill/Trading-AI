import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

kivy.require('1.10.0')


# from kivy.app import App
# from kivy.uix.button import Label
# from kivy.uix.widget import Widget
# from kivy.graphics import Rectangle, Color

class MainScreen(GridLayout):
    def __init__(self, **var_args):
        super(MainScreen, self).__init__(**var_args)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=True)
        self.add_widget(self.username)

        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.add_widget(Label(text='Confirm password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class TradingAI(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    TradingAI().run()