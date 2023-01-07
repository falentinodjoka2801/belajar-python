from tkinter import *

_root   =   Tk()
_root.geometry('200x300')
_root.title('Main')

_l  =   Label(_root, text='This is root window')

_topLevel   =   Toplevel()
_topLevel.geometry('180x100')
_topLevel.title('Top Level')
_l2     =   Label(_topLevel, text='This is toplevel window')

_l.pack()
_l2.pack()

_topLevel.mainloop()