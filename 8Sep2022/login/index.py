from ctypes import sizeof
from math import ceil
from tkinter import *
from tkinter import messagebox
from requests import post, get

_root   =   Tk()

_username   =   'username'
_password   =   'password'

_defaultUsernameValue   =   'Username'
_defaultPasswordValue   =   'Password'

def _onEnter(event:Event):
    _widget     =   event.widget
    _widgetName =   _widget.winfo_name()

    _defaultValue   =   '';
    if(_widgetName == _username):
        _defaultValue   =   _defaultUsernameValue
    
    if(_widgetName == _password):
        _defaultValue   =   _defaultPasswordValue

    if(_widget.get() == _defaultValue):
        _widget.delete(0, 'end')

def _onLeave(event:Event):
    _widget     =   event.widget
    _widgetName =   _widget.winfo_name()

    _defaultValue   =   ''
    if(_widgetName == _username):
        _defaultValue   =   _defaultUsernameValue
    
    if(_widgetName == _password):
        _defaultValue   =   _defaultPasswordValue

    if(len(_widget.get()) <= 0):
        _widget.insert(0, _defaultValue)

def _onSubmit():
    _usernameVal   =   _usernameEntry.get()
    _passwordVal   =   _passwordEntry.get()

    _url        =   'https://api.pancabudi.ac.id/api/autentikasi/sahabat-unpab'
    _formData   =   {'username':_usernameVal, 'password':_passwordVal}
    _login      =   post(_url, data=_formData)

    _response   =   _login.json()
    _status     =   _response['status']
    _message    =   _response['message']
    _data       =   _response['data']

    if(_status):
        _token  =   _data['token']

        _urlListSahabatUNPAB        =   f'https://api.pancabudi.ac.id/api/sahabat-unpab?status=1&kelamin=L'
        _headers                    =   {'Authorization':f'Bearer {_token}'}
        _listSahabatUNPABRequest    =   get(_urlListSahabatUNPAB, headers=_headers)

        _response           =   _listSahabatUNPABRequest.json()
        _listSahabatUNPAB   =   _response['data']

        _successScreen  =   Toplevel(_root)
        _successScreen.title('Login Success')
        _successScreen.geometry(f'300x150+{_xPosition}+{_yPosition}')

        _hScrollbar     =   Scrollbar(_successScreen, orient=HORIZONTAL)
        _vScrollbar     =   Scrollbar(_successScreen, orient=VERTICAL)
        
        _nomorUrutHeaderLabel       =   Label(_successScreen, text='No')
        _nomorUrutHeaderLabel.grid(row=0, column=0, sticky=E)

        _namaHeaderLabel            =   Label(_successScreen, text='Nama Pembawa')
        _namaHeaderLabel.grid(row=0, column=1, sticky=W)

        _nomorPembawaHeaderLabel    =   Label(_successScreen, text='Nomor Pembawa')
        _nomorPembawaHeaderLabel.grid(row=0, column=2, sticky=E)

        _numRows    =   len(_listSahabatUNPAB)
        for _rowIndex in range(_numRows):
            _nomorUrutLabel     =   Label(_successScreen, text=(_rowIndex + 1))
            _nomorUrutLabel.grid(row=(_rowIndex + 1), column=0, sticky=E)

            _namaLabel  =   Label(_successScreen, text=_listSahabatUNPAB[_rowIndex]['pembNama'])
            _namaLabel.grid(row=(_rowIndex + 1), column=1, sticky=W)

            _nomorPembawaLabel  =   Label(_successScreen, text=_listSahabatUNPAB[_rowIndex]['pembNomor'])
            _nomorPembawaLabel.grid(row=(_rowIndex + 1), column=2, sticky=E)

        _successScreen.mainloop()
    else:
        messagebox.showinfo(title='Login Gagal', message=_message)

_screenWidth    =   _root.winfo_screenwidth()
_screenHeight   =   _root.winfo_screenheight()
_rootScreenWidth    =   925
_rootScreenHeight   =   500

_xPosition  =   ceil((_screenWidth / 2) - (_rootScreenWidth / 2))
_yPosition  =   ceil((_screenHeight / 2) - (_rootScreenHeight / 2))

_root.resizable(False, False)
_root.title('Login System')
_root.config(bg='#fff')
_root.geometry(f'{_rootScreenWidth}x{_rootScreenHeight}+{_xPosition}+{_yPosition}')

_formFrameWidth     =   ceil(_rootScreenWidth / 2)

_container  =   Frame(background='#fff', width=_rootScreenWidth, height=_rootScreenHeight)
_container.pack(ipadx=1)

_loginImage         =   PhotoImage(file='8Sep2022/login/img/login.png')
_loginImageLabel    =   Label(_container, image=_loginImage, bg='#fff')
_loginImageLabel.pack(side=LEFT)

_formFrame  =   Frame(_container, width=_formFrameWidth, height=_rootScreenHeight, bg='#fff')
_formFrame.pack(side=LEFT)

_formContainerFrame =   Frame(_formFrame, width=_formFrameWidth-75.0, height=ceil(_rootScreenHeight/1.5), bg='#fff')
_formContainerFrame.place(anchor=CENTER, relx=.5, rely=.5)

_headingLabel   =   Label(_formContainerFrame, text='Sign In', fg='#66cc99', bg='#fff', font=('Microsoft YaHei UI Light', 25, 'bold'))
_headingLabel.place(anchor=CENTER, relx=.5, rely=.15)

_usernameEntry  =   Entry(_formContainerFrame, border=0, bg='#fff', name=_username)
_usernameEntry.insert(0, _defaultUsernameValue)
_usernameEntry.place(anchor=NW, rely=.30, relwidth=1.0)
_usernameEntry.bind('<FocusIn>', _onEnter)
_usernameEntry.bind('<FocusOut>', _onLeave)
Frame(_formContainerFrame, width=_formFrameWidth, height=2, bg='#000').place(anchor=NW, rely=0.4)

_passwordEntry  =   Entry(_formContainerFrame, border=0, bg='#fff', name=_password, show='*')
_passwordEntry.insert(0, 'Password')
_passwordEntry.place(anchor=NW, rely=0.525, relwidth=1.0)
_passwordEntry.bind('<FocusIn>', _onEnter)
_passwordEntry.bind('<FocusOut>', _onLeave)
Frame(_formContainerFrame, width=_formFrameWidth, height=2, bg='#000').place(anchor=NW, rely=0.625)

_buttonSubmit   =   Button(_formContainerFrame, text='Sign In', fg='#fff', bg='#66cc99', height=2, border=0, command=_onSubmit)
_buttonSubmit.place(anchor=NW, rely=.75, relwidth=1.0)

Label(_formContainerFrame, text='Don\'t have an account?', bg='#fff').place(anchor=CENTER, relx=.5, rely=.975)

_root.mainloop()