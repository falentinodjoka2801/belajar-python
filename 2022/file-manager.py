from tkinter import *
import tkinter.filedialog as fD
import tkinter.messagebox as mB

import os
import shutil

def open_file():
    mB.showinfo('Heh!', message='Trus gua harus ngomong waw gitu?')
    # try:
    #     file    =   fD.askopenfilename(title='Choose a file of any type', filetypes=[("All Files", "*.*")])
    #     os.startfile(os.path.abspath(file))
    # except:
    #     mB.showwarning(title='Warning!', message='Some errors occured!')

def copy_file():
    fileToCopy      =   fD.askopenfilename(title='Choose a file to copy', filetypes=[('All Files', '*.*')])
    dirToCopyTo     =   fD.askdirectory(title='In which folder to copy to?')

    try:
        shutil.copy(fileToCopy, dirToCopyTo)
        mB.showinfo(title='File copied!')
    except:
        mB.showerror(title='Error', message='We were unable to copy your file to desired location! Please try again!')

def delete_file():
    file    =   fD.askopenfilename(title='Choose a file to delete', filetypes=[("Any files", "*.*")])
    os.remove(os.path.abspath(file))
    mB.showinfo(title='File deleted!', message='Your desired file has been deleted')

def open_folder():
    folder  =   fD.askdirectory(title='Select Folder to Open');
    os.startfile(folder)

def delete_folder():
    folderToDelete  =   fD.askdirectory(title='Choose a folder to delete')
    os.rmdir(folderToDelete)
    mB.showinfo(title='Folder deleted!', message='Your desired folder has been deleted!')

def move_folder():
    folderToMove    =   fD.askdirectory(title='Select the dolder you want to move');
    mB.showinfo(message='You just selected the folder to move, now please select the desired destination where you want to move the folder to')
    destination     =   fD.askdirectory(title='Where to move the folder to?')

    try:
        shutil.move(folderToMove, destination)
        mB.showinfo(title='Folder moved!', message='Your desired folder has been moved to the location you wanted!')
    except:
        mB.showerror(title='Error', message='We could not move your folder. Please make sure that the destination exists!')

def list_files_in_folder():
    try:
        i = 0
        folder = fD.askdirectory(title='Select the folder whose files you want to list')
        files = os.listdir(os.path.abspath(folder))

        list_files_wn = Toplevel(root)
        list_files_wn.title('Files in folder')
        list_files_wn.geometry('250x250')
        list_files_wn.resizable(0, 0)

        listbox = Listbox(list_files_wn, selectbackground='Steelblue', font=('Georgia', 10))
        listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

        scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill="both")

        listbox.config(yscrollcommand=scrollbar.set)

        while i < len(files):
            listbox.insert(END, files[i])
            i += 1
    except:
        mB.showinfo('Terjadi Error', 'Oops! Something went wrong!');


try:
    title       =   'Data Flair File Manager'
    background  =   'Yellow'

    buttonFont          =   ('Times New Roman', 13)
    buttonBackground    =   'Turquoise'

    root    =   Tk()
    root.title(title)
    root.geometry('250x400')
    root.resizable(1, 1)
    root.config(bg=background)

    Label(root, text=title, font=('Comic Sans MS', 15), bg=background, wraplength=250).place(x=20, y=0)
    Button(root, text='Open a file', width=20, font=buttonFont, bg=buttonBackground, command=open_file).place(x=30, y=50)
    Button(root, text='List all files in a folder', width=20, font=buttonFont, command=list_files_in_folder).place(x=30, y=330)
    root.update()
    root.mainloop()
except KeyboardInterrupt as kI:
    mB.showinfo('Keyboard Interruption', 'Anda menekan ctrl+c sehingga aplikasi tertutup!')