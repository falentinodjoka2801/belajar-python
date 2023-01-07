from kivy.app import App
from kivy.uix.label import Label

class MyFirstKivyApp(App):
    def build(self):
        return Label(text='Hello World!')

_app    =   MyFirstKivyApp()
_app.run()