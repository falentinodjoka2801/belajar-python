from tkinter import *

_rootWidth  =   900
_rootHeight =   450

_root   =   Tk()
_root.title('Positioning Widgets with Place Method')
_root.geometry(f'{_rootWidth}x{_rootHeight}')

_buttonA        =   Button(_root, text='Ayam Kampung', height=2)
# _buttonAWidth   =   _buttonA.winfo_width()
# _persentaseButtonAWidth =   _buttonAWidth / _rootWidth * 100;   

# print(_buttonAWidth)
# print(_persentaseButtonAWidth)

_buttonA.place(anchor=CENTER, relwidth=0.5, relx=0.5, rely=0.5)

_root.mainloop()