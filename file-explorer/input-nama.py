from tkinter import *
from tkinter import messagebox as mB

def _onSubmitted():
    _name   =   _inputNamaLengkap.get()
    _showInfo   =   mB.showinfo(title='Hello', message='Hello '+_name+'!')
    _topLevel   =   Toplevel()
    _topLevel.mainloop()

#semua function yang berasal dari TKinter harus didefinisikan setelah adanya inisialisasi objek Tk()
_root   =   Tk()
_icon   =   PhotoImage(file='../assets/icon/laukpauk-icon.png')

_root.title('Perkenalan Diri')
_root.iconphoto(False, _icon)

_label  =   Label(text='Nama Lengkap')
_label.pack()

_inputNamaLengkap   =   Entry(width=100)
_inputNamaLengkap.pack()

_submitBtn  =   Button(text='Submit', bg='#28a745', fg='#fff', command=_onSubmitted)
_submitBtn.pack()

_root.mainloop()