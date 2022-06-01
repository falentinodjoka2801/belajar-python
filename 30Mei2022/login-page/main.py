from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from requests import post

Window.size     =   (300, 450)

class LoginApp(MDApp):
    dialog  =   None

    def build(self):
        self.theme_cls.theme_style      =   'Dark'
        self.theme_cls.primary_palette  =   'Indigo'
        self.theme_cls.accent_palette   =   'Blue'
        
        _loginForm  =   './views/login-form.kv'
        return Builder.load_file(_loginForm)

    def login(self):
        _inputEl    =   self.root.ids
        _usernameEl =   _inputEl.username
        _passwordEl =   _inputEl.password

        _username   =   _usernameEl.text
        _password   =   _passwordEl.text

        _url    =   'http://localhost/laukpauk/api/auth/auth'
        _data   =   {'username' : _username, 'password' : _password}
        _authenticationResponse =   post(_url, data=_data)
        
        _jsonResponse   =   _authenticationResponse.json()
        print(_jsonResponse)

LoginApp().run()