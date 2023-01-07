from tkinter import *

_root   =   Tk()
_root.geometry('600x300')
_root.title('Pack')

_buttonA    =   Button(_root, text='Ayam Kampung')
_buttonA.pack(side=LEFT)

_buttonB    =   Button(_root, text='Babi Hutan')
_buttonB.pack(side=TOP)

_buttonC    =   Button(_root, text='Cacing Tanah')
_buttonC.pack(side=RIGHT)

_buttonD    =   Button(_root, text='Domba')
_buttonD.pack(side=BOTTOM)

_root.mainloop()