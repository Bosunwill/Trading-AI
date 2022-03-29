import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

class CanvasWidget(Widget):
    def __init__(self, **kwargs):
        super(CanvasWidget, self).__init__(**kwargs)
        with self.canvas:
            Color(.234, .456, .678, .8)
            self.rect = Rectangle(pos = self.center, size = (self.width / 2., self.height / 2.))
            self.label = Label(text = "Trading AI App", halign = "center", valign = "center")

            self.bind(pos = self.update_rect, size = self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.label.pos = self.pos
        self.rect.size = self.size

# class LabelWidget(GridLayout):
#     bones = 0
#     def __init__(self, **kwargs):
#         super(LabelWidget, self).__init__(**kwargs)
#         self.label_text = Label(text = "Trading AI App")
#         self.add_widget(self.label_text)
#         def update_text(self, text):
#             LabelWidget.bones = text
#             self.label_text.text = str(LabelWidget().bones)
#             LabelWidget.text = str(LabelWidget().bones)

class TradingAI(App):
    def build(self):
        canvas = CanvasWidget()
        return canvas


tradingAI = TradingAI()
tradingAI.run()