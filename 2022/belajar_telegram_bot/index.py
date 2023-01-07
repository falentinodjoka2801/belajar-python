from tkinter import *

from bot.pancabudi_bot import PancaBudi

_root   =   Tk()
_root.title('Telegram with Python')
_root.geometry('500x350')

try:
    _pbb        =   PancaBudi()

    #button
    def _start():
        _pbb.start()
        _startButton['state']   =   'disabled'
        _stopButton['state']    =   'normal'

    def _stop():
        _pbb.stop()
        _startButton['state']   =   'normal'
        _stopButton['state']    =   'disabled'

    _startButton    =   Button(text='Start Telegram Bot', command=_start, 
                            background='#28a745', border=0, height=2, foreground='#fff',
                            state='normal')
    _startButton.pack()

    _stopButton     =   Button(text='Stop Telegram Bot', command=_stop, 
                            background='#dc3545', border=0, height=2, foreground='#fff',
                            state='disabled')
    _stopButton.pack()

    _quitButton     =   Button(text='Quit', command=quit, 
                            background='#282a35', border=0, height=2, foreground='#fff',
                            state='normal')

    _quitButton.pack()

    _root.mainloop()
except:
    print('There is something wrong!')