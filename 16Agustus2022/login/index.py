from tkinter import *
from tkinter import messagebox

_root   =   Tk()

_root.title('Login')
_root.geometry('925x500+300+200')
_root.configure(bg='#fff')
_root.resizable(False, False)

_img    =   PhotoImage(file='16Agustus2022/login/login.png')
Label(_root, image=_img, bg='#fff').place(x=50, y=50)

_frame  =   Frame(_root, width=350, height=350, bg='#fff')
_frame.place(x=480, y=70)

_font       =   ('Microsoft YaHei UI Light', 23, 'bold')
_fontSize11 =   ('Microsoft YaHei UI Light', 11)  
_fontSize9 =   ('Microsoft YaHei UI Light', 9)  

_heading    =   Label(_frame, text='Sign In', fg='#57a1f8', bg='#fff', font=_font)
_heading.place(x=100, y=5)

_username   =   Entry(_frame, width=25, border=0, fg='#000', bg='#fff', font=_fontSize11)
_username.place(x=30, y=80)
_username.insert(0, 'Username')
Frame(_frame, width=295, height=2, bg='#000').place(x=25, y=107)

_password   =   Entry(_frame, width=25, border=0, fg='#000', bg='#fff', font=_fontSize11)
_password.place(x=30, y=150)
_password.insert(0, 'Password')
Frame(_frame, width=295, height=2, bg='#000').place(x=25, y=177)

Button(_frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='#fff', border=0).place(x=35, y=204)

_label  =   Label(_frame, text='Don\'t have an account?', fg='#000', bg='#fff', font=_fontSize9)
_label.place(x=75, y=270)

_root.mainloop()