import tkinter as tk
import main
from tkinter import filedialog
import os




# Main window
root = tk.Tk()

# Defines window title
root.title('Simple Search')

# Defines window default window size
root.geometry('1000x200')

# Two labels - 'from which word', 'to which word'
l_what_to_change = tk.Label(root, text='Kas jamaina?', font='monospace 12').grid(row=0, pady=(10, 10))
l_change_to_what = tk.Label(root, text='Uz ko?', font='monospace 12').grid(row=1)


# Function for browsing files and folders
def dir_dialog():
    global directory
    directory = filedialog.askdirectory(initialdir="/home/meldzha/PycharmProjects/", title="Izvelies mapi")
    path_title = tk.Label(root, text='Izveleta mape:', font='monospace 12 bold').grid(row=0, column=3, pady=(10, 0))
    path_label = tk.Label(root, text=directory, font='monospace 11').grid(row=1, column=3)
    file_list_title = tk.Label(root, text='Faili mape:', font='monospace 12 bold').grid(row=2, column=3, pady=(10, 0))
    file_list_label = tk.Label(root, text=os.listdir(directory), font='monospace 11').grid(row=3, column=3)
    os.chdir(directory)


# Browse files and folders
l_browse_dirs = tk.Label(root, text='Meklet diska:', font='monospace 12').grid(row=0, column=2, padx='30')
btn_browse_files = tk.Button(root, text='Meklet', command=dir_dialog).grid(row=1, column=2)

# Two entry fields (String entries)
e1 = tk.Entry(root)
e2 = tk.Entry(root)

# Entries placement in window
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Quit and Accept buttons
tk.Button(root, text='Iziet', command=root.quit, width=9).grid(row=4, column=1)
tk.Button(root, text='Apstiprinat', command=lambda:[main.replace_words(), change_accepted()]).grid(row=3, column=1, pady=(10, 0))

# 'Acceptance' label that pops up when the text has been changed
def change_accepted():
    accepted_label = tk.Label(root, text='Vards veiksmigi nomainits!').grid(row=5, column=1)

root.mainloop()


