from tkinter import *
from tkinter import messagebox as mB

def _onSubmitted():
    _name   =   _inputNamaLengkap.get()
    _topLevel       =   Toplevel()
    _topLevel.title('Greeting')

    _greetingLabel  =   Label(text='Hello, '+_name, master=_topLevel)
    _greetingLabel.pack()

    _topLevel.mainloop()

#semua function yang berasal dari TKinter harus didefinisikan setelah adanya inisialisasi objek Tk()
_root   =   Tk(screenName='Index')
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