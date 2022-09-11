from tkinter import *
from tkinter import messagebox
from math import ceil

#{

windowWidth     =   925
windowHeight    =   500

window  =   Tk()
window.title('Sign Up')
window.geometry(f'{windowWidth}x{windowHeight}+300+185')
window.configure(bg='#fff')

container   =   Frame(window, width=windowWidth, height=windowHeight, bg='#fff')
container.pack(padx=35)

img     =   PhotoImage(file='11Sep2022/registrasi/img/login.png')
imgLabel    =   Label(container, image=img, bg='#fff')
imgLabel.pack(side=LEFT)

formFrame   =   Frame(container, bg='#fff', width=windowWidth, height=windowHeight)
formFrame.pack(side=LEFT)

formContainer   =   Frame(formFrame, bg='#fff')
formContainer.place(anchor=CENTER, relx=.5, rely=.5, relwidth=.9, relheight=.8)

headingLabel     =   Label(formContainer, text='Sign Up', bg='#fff', font=('Microsoft Yahei UI Light', 25, 'bold'), fg='#66cc99')
headingLabel.place(anchor=CENTER, relx=.5, rely=.1)

usernameEntry   =   Entry(formContainer, border=0, bg='#fff')
usernameEntry.place(anchor=NW, relwidth=1, relheight=.12, rely=.3)
usernameEntry.insert(0, 'Username')
Frame(formContainer, bg='#000', height=2, width=windowWidth).place(anchor=NW, rely=.415)

passwordEntry   =   Entry(formContainer, border=0, bg='#fff')
passwordEntry.place(anchor=NW, relwidth=1.0, relheight=.12, rely=.45)
passwordEntry.insert(0, 'Password')
Frame(formContainer, height=2, bg='#000').place(rely=.565, anchor=NW, relwidth=1.0)

passwordConfirmEntry    =   Entry(formContainer, bg='#fff', border=0)
passwordConfirmEntry.place(anchor=NW, relwidth=1.0, relheight=.12, rely=.6)
passwordConfirmEntry.insert(0, 'Password Confirmation')
Frame(formContainer, height=2, bg='#000').place(relwidth=1.0, anchor=NW, rely=.715)

buttonSubmit    =   Button(formContainer, bg='#66cc99', border=0, fg='#fff', text='Sign Up')
buttonSubmit.place(anchor=NW, relwidth=1.0, relheight=.12, rely=.8)

window.mainloop()