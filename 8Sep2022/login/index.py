from math import ceil
from tkinter import *
from tkinter import messagebox

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

_loginImage         =   PhotoImage(file='8Sep2022/login/img/login.png')
_loginImageLabel    =   Label(_root, image=_loginImage, bg='#fff')
_loginImageLabel.place(x=50, y=50)

_formFrameWidth     =   ceil(_rootScreenWidth / 2)

_formFrame  =   Frame(_root, width=_formFrameWidth, height=_rootScreenHeight, bg='#fff')
_formFrame.place(x=_formFrameWidth)

_entryWidth     =   _formFrame.winfo_reqwidth()

_uLabel     =   Label(_formFrame, text='Username')
_uLabel.grid(row=0, column=0, sticky='w')
_uEntry     =   Entry(_formFrame, width=_entryWidth)
_uEntry.grid(row=0, column=1)

_pLabel     =   Label(_formFrame, text='Password')
_pLabel.grid(row=1, column=0, sticky='w')
_pEntry     =   Entry(_formFrame, width=_entryWidth)
_pEntry.grid(row=1, column=1)

# _headingLabel   =   Label(_formFrame, text='Sign In', fg='#66cc99', bg='#fff', font=('Microsoft YaHei UI Light', 25, 'bold'))
# _headingLabel.place(x=ceil(_formFrame.winfo_reqwidth()/2 - _headingLabel.winfo_reqwidth()/2), y=50)


# _usernameEntry  =   Entry(_formFrame, border=0, bg='#fff', width=_entryWidth)
# _usernameEntry.place(y=125)
# _usernameEntry.insert(0, 'Username')
# Frame(_formFrame, width=_formFrameWidth, height=2, bg='#000').place(y=150)

# _passwordEntry  =   Entry(_formFrame, border=0, bg='#fff', width=_entryWidth)
# _passwordEntry.place(y=185)
# _passwordEntry.insert(0, 'Password')
# Frame(_formFrame, width=_formFrameWidth, height=2, bg='#000').place(y=215)

# _buttonSubmit   =   Button(_formFrame, text='Sign In', bg='#66cc99', height=2, border=0, padx=25, fg='#fff', command=_showLoginForm)
# _buttonSubmit.place(x=ceil(_formFrame.winfo_reqwidth()/2 - _buttonSubmit.winfo_reqwidth()/2), y=250)

_root.mainloop()