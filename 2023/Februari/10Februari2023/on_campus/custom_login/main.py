import tkinter
import customtkinter as ct
from PIL import Image, ImageTk

ct.set_appearance_mode('dark')
ct.set_default_color_theme('green')

app =   ct.CTk()
app.geometry('600x440')
app.title('Login Page')

img1    =   ImageTk.PhotoImage(Image.open('2023/Februari/10Februari2023/on_campus/custom_login/pattern.png'))
l1  =   ct.CTkLabel(master=app, image=img1)
l1.pack()

frame = ct.CTkFrame(master=app, width=320, height=360)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = ct.CTkLabel(master=frame, text='Log into your Account', font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1 = ct.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2 = ct.CTkEntry(master=frame, width=220, placeholder_text='Password')
entry2.place(x=50, y=165)

l2 = ct.CTkLabel(master=frame, text='Forget password', font=('Century Gothic', 12))
l2.place(x=165, y=195)

button1 = ct.CTkButton(master=frame, width=220, text='Login', corner_radius=6)
button1.place(x=50, y=240)

img2    =   ct.CTkImage(Image.open('2023/Februari/10Februari2023/on_campus/custom_login/Google__G__Logo.svg.webp').resize((20, 20), Image.ANTIALIAS))
img3    =   ct.CTkImage(Image.open('2023/Februari/10Februari2023/on_campus/custom_login/124010.png').resize((20, 20), Image.ANTIALIAS))

button2 =   ct.CTkButton(master=frame, image=img2, text='Google', width=100, height=20, corner_radius=6, compound='left', text_color='Black')
button2.place(x=50, y=290)

button3 =   ct.CTkButton(master=frame, image=img3, text='Facebook', width=100, height=20, corner_radius=6, compound='left', text_color='Black')
button3.place(x=170, y=290)

app.mainloop()