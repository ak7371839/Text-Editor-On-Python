# Use Of a variable a this
'''
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from turtle import window_width
from tkinter import ttk
'''

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from turtle import window_width
from tkinter import ttk

root = Tk(className="|--Text Editor By CodeWithArpit--|")
textpad = scrolledtext.ScrolledText(root, width=100, height=80)

# Creating a menu & define function for each menu item

def open_command():
    file = filedialog.askopenfile(parent=root, mode='rb', title='Select a File')
    if file != None:
        contents = file.read()
        textpad.insert('1.0', contents)
        file.close()

def save_command():
    file = filedialog.asksaveasfile(mode='w') #check
    if file != None:
        # slice off the last character from get, as an extra return is added
        data = textpad.get('1.0', END + '-1c')
        file.write(data)
        file.close()

def exit_command():
    if messagebox.askokcancel('Quit','Do you really want to quit'):
        root.destroy()

def about_command():
    label = messagebox.showinfo('About','''This Text Editor is created by CodeWithArpit
 this is a greatest text editor created in python using tkinter for GUI''')

def new_window():
    import texteditor2

def cut():
    textpad.event_generate("<<Cut>>")

def resize_win():
    root.geometry("800x600")

def ps():
    ps=Tk()
    ps.geometry("800x600")
    ps.title("Python Statment")
    ps.resizable(False,False)
    notebook = ttk.Notebook(ps)

    tab1 = Frame(notebook)
    tab2 = Frame(notebook)
    tab3 = Frame(notebook)
    notebook.add(tab1,text="Print")
    notebook.add(tab2,text="Variable")
    notebook.add(tab3,text="Create GUI in python")

    l1 = Label(tab1,text="Print Statment a print of a code a python the code of a print. print('Hello World')").place(x=0,y=0)
    l2 = Label(tab2,text="Variable is a store is a data type form a variable code (a = 1) this is a variable code.").place(x=0,y=0)
    l2 = Label(tab3,text="""GUI Create code a from tkinter import *
                        root=Tk()
                            root.mainloop()""").place(x=0,y=0)
    notebook.pack(expand=True,fill="both")
    ps.mainloop()

def infobar():
    # new,new window,open,save,exit
    messagebox.showinfo("Menu Work In New","New-->New Workspace")
    messagebox.showinfo("Menu Work In New Window","New Window-->New Window Open a texteditor")
    messagebox.showinfo("Menu Work In Open","Open-->Open A File")
    messagebox.showinfo("Menu Work in Save","Save-->Save to a code file")
    messagebox.showinfo("Menu Work in Exit","Exit-->Exit to the editor")
    mi = messagebox.askyesno("Menu Info","Acces To The Menu Information")
    # print(mi)
    if(mi==True):
        messagebox.showinfo("Best","Best of Luck For Editor")
    else:
        infobar()

def infos():
    messagebox.showinfo("Software Info","The Software Code in from computer arpit website www.coderweb.com in a software scorcode")


# menues work


menu = Menu(root)
root.config(menu=menu)
# Adding menues
filemenu = Menu(menu)
editmenu = Menu(menu)
codemenu = Menu(menu)
infomenu = Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
menu.add_cascade(label='Edit',menu=editmenu)
menu.add_cascade(label="Information",menu=infomenu)
menu.add_cascade(label='Code',menu=codemenu)

# file menu

filemenu.add_command(label='New')
filemenu.add_command(label='New Window',command=new_window)
filemenu.add_command(label='Open...',command=open_command)
filemenu.add_command(label='Save',command=save_command)
filemenu.add_separator() # new command
filemenu.add_command(label='Exit',command=exit_command)

# edit menu

editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=cut)
editmenu.add_separator()
editmenu.add_command(label="Resize Window",command=resize_win)

# code menu

codemenu.add_command(label="Python Statment",command=ps)


# Info menu

infomenu.add_command(label="Information in this is a menu bar",command=infobar)
infomenu.add_command(label="Information in Software",command=infos)                 


# help menu

helpmenu = Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)

helpmenu.add_command(label='About...', command=about_command)

# And Menus

textpad.pack(fill=X)
root.mainloop()
