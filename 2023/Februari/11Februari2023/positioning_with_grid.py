from tkinter import *

root    =   Tk()

root.geometry('250x200')

Label(root, text='Position 1', width=10, bg='red').grid(row=0, column=0)
Label(root, text='Position 2', width=10, bg='green').grid(row=0, column=1)
Label(root, text='Position 3', width=10, bg='blue').grid(row=1, column=0)
Label(root, text='Position 4', width=10, bg='yellow').grid(row=1, column=1)
Label(root, text='Position 5', bg='purple', width=10).grid(row=2, column=0)
Label(root, text='Position 6', width=10, bg='#66cc99').grid(row=2, column=1)

root.mainloop()