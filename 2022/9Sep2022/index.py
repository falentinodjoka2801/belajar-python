from tkinter import *

_root   =   Tk()
_root.title('Positioning Widget with pack() method')

_redLabel   =   Label(_root, text='Red', bg='red', fg='#fff')
_redLabel.pack(side=RIGHT)

_greenLabel     =   Label(_root, text='Green', bg='green', fg='#fff')
_greenLabel.pack(side=RIGHT)

_purpleLabel    =   Label(_root, text='Purple', bg='purple', fg='#fff')
_purpleLabel.pack(side=RIGHT)

_root.mainloop()