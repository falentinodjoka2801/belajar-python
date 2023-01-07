from tkinter import *
from math import ceil

_root   =   Tk()
_root.title('Login')
_root.resizable(False, False)
_root.configure(bg='#fff')

_screenWidth    =   _root.winfo_screenwidth()
_screenHeight   =   _root.winfo_screenheight()

_pageWidth  =   900
_pageHeight =   500

_xPosition  =   (_screenWidth / 2) - (_pageWidth / 2)
_xPosition  =   ceil(_xPosition)
_yPosition  =   (_screenHeight / 2) - (_pageHeight / 2)
_yPosition  =   ceil(_yPosition)

_root.geometry(f'{_pageWidth}x{_pageHeight}+{_xPosition}+{_yPosition}')

_loginImg       =   PhotoImage(file='21Agustus2022/login.png')
_loginImgLabel  =   Label(_root, image=_loginImg, bg='#fff')
_loginImgLabel.place(x=((_pageWidth/4) - (_loginImg.width()/2)), y=((_pageHeight/2) - (_loginImg.height()/2)))

_formFrameWidth     =   _pageWidth/2
_formFrameHeight    =   _pageHeight/2

_formFrame  =   Frame(_root, width=_formFrameWidth, height=_formFrameHeight, bg='#fff')
_formFrame.pack(side='right', padx=35)

_formTitle  =   Label(_formFrame, text='Sign In', bg='#fff', font=('Microsoft YaHei UI Light', 23, 'bold'))
_formTitle.place(x=((_formFrameWidth/2) - (_formTitle.winfo_reqwidth()/2)))

_username   =   Entry(_formFrame, textvariable=StringVar(), width=(ceil(_formFrameWidth)), bg='#fff', borderwidth=0)
_username.place(y=75)

_password   =   Entry(_formFrame, width=(ceil(_formFrameWidth)), bg='#fff', borderwidth=0)
_password.place(y=125)


_root.mainloop()