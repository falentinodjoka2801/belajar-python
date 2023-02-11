import customtkinter as ct
from PIL import Image, ImageTk
from tkinter import Event

ct.set_appearance_mode('dark')
ct.set_default_color_theme('green')

def on_submit():
    username    =   username_entry.get()
    password    =   password_entry.get()
    print(f'username = {username}, password = {password}')

def on_focus_in(event: Event):
    print(event.widget.get())

root    =   ct.CTk()
root.title('Login Page')
root.geometry('600x440')

background_image    =   ImageTk.PhotoImage(Image.open('assets/pattern.png'))
ct.CTkLabel(root, image=background_image).pack()

form_frame  =   ct.CTkFrame(master=root, width=350, height=375, corner_radius=6)
form_frame.place(relx=0.5, rely=0.5, anchor=ct.CENTER)

form_container_frame    =   ct.CTkFrame(form_frame, bg_color='transparent', fg_color='transparent', width=50, height=50)
form_container_frame.pack(padx=25, pady=25)

title   =   ct.CTkLabel(master=form_container_frame, text='Login to your account', text_color='#fff', font=('Century Gothic', 20))
title.pack(pady=(0, 25))

username_entry  =   ct.CTkEntry(form_container_frame, placeholder_text='Username', width=250, height=35,)
username_entry.bind('<FocusIn>', on_focus_in)
username_entry.pack(pady=(0, 10))

password_entry  =   ct.CTkEntry(form_container_frame, placeholder_text='Password', width=250, height=35)
password_entry.bind('<FocusIn>', on_focus_in)
password_entry.pack(pady=(0, 10))

sign_in_button  =   ct.CTkButton(form_container_frame, text='Login', height=35, width=250, command=on_submit)
sign_in_button.pack(pady=(0, 7.5))

forget_password_label   =   ct.CTkLabel(form_container_frame, text='Forgot Password', text_color='#fff')
forget_password_label.pack(side=ct.RIGHT)

root.mainloop()