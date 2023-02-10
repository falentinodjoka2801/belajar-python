import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('green')

app =   customtkinter.CTk()
app.geometry('600x440')
app.title('Login')

img1    =   ImageTk.PhotoImage(Image.open())

app.mainloop()