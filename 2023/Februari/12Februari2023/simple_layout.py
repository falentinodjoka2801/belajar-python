from tkinter import *

root    =   Tk()
root.title('Basic GUI Layout')
root.maxsize(600, 900)
root.config(bg='skyblue')

left_frame  =   Frame(root, width=200, height=400, background='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame =   Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

Label(left_frame, text='Original Image').grid(row=0, column=0, padx=5, pady=5)

image   =   PhotoImage(file='assets/124010.png')
original_image  =   image.subsample(3, 3)
Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)

Label(right_frame, image=image).grid(row=0, column=0, padx=5, pady=5)

root.mainloop()