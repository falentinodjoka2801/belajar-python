from math import ceil
from tkinter import *
from tkinter import messagebox
from typing import Container

_root   =   Tk()

# def _showLoginForm():
#     print('Hello')

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

_formContainerFrame =   Frame(_formFrame, width=_formFrameWidth-50, height=ceil(_rootScreenHeight/1.5), bg='#fff')
_formContainerFrame.place(anchor=CENTER, relx=.5, rely=.5)

_headingLabel   =   Label(_formContainerFrame, text='Sign In', fg='#66cc99', bg='#fff', font=('Microsoft YaHei UI Light', 25, 'bold'))
_headingLabel.place(anchor=CENTER, relx=.5, rely=.15)

_usernameEntry  =   Entry(_formContainerFrame, border=0, bg='#fff')
_usernameEntry.insert(0, 'Username')
_usernameEntry.place(anchor=NW, rely=.30, relwidth=1.0)
Frame(_formContainerFrame, width=_formFrameWidth, height=2, bg='#000').place(anchor=NW, rely=0.4)

_passwordEntry  =   Entry(_formContainerFrame, border=0, bg='#fff')
_passwordEntry.insert(0, 'Password')
_passwordEntry.place(anchor=NW, rely=0.525, relwidth=1.0)
Frame(_formContainerFrame, width=_formFrameWidth, height=2, bg='#000').place(anchor=NW, rely=0.625)

_buttonSubmit   =   Button(_formContainerFrame, text='Sign In', fg='#fff', bg='#66cc99', height=2, border=0)
_buttonSubmit.place(anchor=NW, rely=.75, relwidth=1.0)

_root.mainloop()