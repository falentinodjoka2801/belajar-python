# from tkinter import *

# root    =   Tk()

# _iconImage  =   PhotoImage(file='../assets/icon/laukpauk-icon.png')

# root.title('File Explorer - Tino')
# root.iconphoto(False, _iconImage)
# root.mainloop()
 
from tkinter import *
from tkinter import messagebox as mB


def _tryToClickMe():
    mB.showinfo(title='Hello', message='Hello brother, are you okay today?')

def _submit():
    _name   =   _nameInput.get()
    mB.showinfo(title='Hello!', message='Hello '+_name+', nice to meet you!')
    _nameInput.delete(0)

_window     =   Tk()
try:
    _label      =   Label(text='Python rocks!')
    _label.pack()

    _button     =   Button(text='Try to click me', width=15, 
                        height=2, bg='#43ac6a', fg='#fff', command=_tryToClickMe)
    _button.pack()

    _nameInput  =   Entry(width=50)
    _nameInput.pack()

    _submitButton   =   Button(text='Submit', bg='#fd7e14', fg='#fff',
                            command=_submit)
    _submitButton.pack()
except:
    print('There is something wrong!')

_window.mainloop()