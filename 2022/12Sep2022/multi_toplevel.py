from tkinter import *

def _openTopLevel1():
    _topLevel1  =   Toplevel(_root)
    _topLevel1.title('Top Level 1')
    _topLevel1.geometry('400x400')
    
    _topLevel1Label     =   Label(_topLevel1, text='This is a Top Level 1 Window')
    _topLevel1Label.pack()

    _topLevel1Button    =   Button(_topLevel1, text='Open TopLevel 2', command=_openTopLevel2)
    _topLevel1Button.pack()

    _topLevel1ExitButton    =   Button(_topLevel1, text='Exit', command=_topLevel1.destroy)
    _topLevel1ExitButton.pack()

    _topLevel1.mainloop()

def _openTopLevel2():
    _topLevel2  =   Toplevel()
    _topLevel2.title('Top Level 2')
    _topLevel2.geometry('300x300')

    _topLevel2Label =   Label(_topLevel2, text='This is a TopLevel2 Window')
    _topLevel2Label.pack()

    _topLevel2Button    =   Button(_topLevel2, text='Exit', command=_topLevel2.destroy)
    _topLevel2Button.pack()

    _topLevel2.mainloop()

_root   =   Tk()
_root.title('Root Window')
_root.geometry('500x500')

_rootLabel  =   Label(_root, text='This is Root Window')
_rootLabel.pack()

_rootButton =   Button(_root, text='Open TopLevel 1', command=_openTopLevel1)
_rootButton.pack()

_root.mainloop()