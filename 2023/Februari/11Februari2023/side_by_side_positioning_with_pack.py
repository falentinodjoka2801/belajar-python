import tkinter as tk

root    =   tk.Tk()

red     =   tk.Label(root, text='Red', bg='red', fg='white')
red.pack(side=tk.LEFT, padx=5, pady=15)

green   =   tk.Label(root, text='Green', bg='green', fg='white')
green.pack(side=tk.LEFT, padx=5, pady=20)

purple  =   tk.Label(root, text='Purple', bg='purple', fg='white')
purple.pack(side=tk.LEFT, padx=5, pady=20)

root.mainloop()