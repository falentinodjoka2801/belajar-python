from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def __init__(self, **args):
        super(LoginScreen, self).__init__(**args)

        self.cols   =   4
        self.add_widget(Label(text='Username'))
        self.username   =   TextInput(multiline=True)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password'))
        self.password   =   TextInput(password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text='Confirm Password'))
        self.confirmPassword    =   TextInput(password=True)
        self.add_widget(self.confirmPassword)

class MyApp(App):
    def build(self):
        return LoginScreen()

MyApp().run()