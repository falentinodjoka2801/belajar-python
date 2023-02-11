from customtkinter import CTk, CTkLabel, CTkFrame, CTkEntry, CTkButton, set_default_color_theme, CTkImage
import tkinter as tk
from PIL import ImageTk, Image

width   =   800
height  =   500

set_default_color_theme('green')

root = CTk()
root.title('Login Page - Sahabat UNPAB')
root.geometry(f'{width}x{height}')

container   =   CTkFrame(root, fg_color='transparent')
container.place(anchor=tk.CENTER, relx=0.5, rely=0.5)

left_container  =   CTkFrame(container, fg_color='transparent')
left_container.pack(side=tk.LEFT, padx=15)

logo_unpab_image    =   Image.open('assets/logo_unpab.png')
CTkLabel(left_container, image=CTkImage(light_image=logo_unpab_image, dark_image=logo_unpab_image, size=(150, 150)), text=None).pack()
CTkLabel(left_container, text='Yayasan Pendidikan Kadirun Yahya', font=('Century Gothic', 20)).pack(pady=(20, 5))
CTkLabel(left_container, text='Universitas Pancabudi Medan', font=('Century Gothic', 16)).pack()
CTkLabel(left_container, text='Jl. Gatot Subtoro KM. 4.5 Sei Sikambing', font=('Century Gothic', 12)).pack()

form_frame  =   CTkFrame(container, fg_color='#fff')
form_frame.pack(side=tk.LEFT, padx=15, ipady=15, ipadx=15)

CTkLabel(form_frame, text='Portal Login', text_color='#222222', font=('Century Gothic', 27)).pack(pady=(25, 5))
CTkLabel(form_frame, text='Sahabat UNPAB', text_color='#444444', font=('Century Gothic', 18)).pack(pady=(0, 25))
username_entry  =   CTkEntry(form_frame, placeholder_text='Username', height=40, width=250)
username_entry.pack(pady=(0, 10))
password_entry  =   CTkEntry(form_frame, placeholder_text='Password', height=40, width=250)
password_entry.pack(pady=(0, 10))
sign_in_button  =   CTkButton(form_frame, text='Sign In', height=40, width=250)
sign_in_button.pack(pady=(5, 25))

root.mainloop()