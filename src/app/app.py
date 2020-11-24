'''
Created on Nov 23, 2020

@author: manso
'''

import tkinter as tk
from tkinter import *
import os

root = tk.Tk()
root.title("Zaezul's Loader")
root.resizable(False, False)

apps = []

# If the text file exists in the path, then use it on start to list previous apps.
if os.path.isfile('Saved Apps.txt'):
    with open('Saved Apps.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

# Adds an app to be run.
def addApp():

    for widget in myframe.winfo_children():
        widget.destroy()


    filenames= filedialog.askopenfilenames(initialdir="/", title="Select File",
                                         filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    root.tk.splitlist(filenames)

    for file in filenames:
        apps.append(file)

    # print(filename)
    for app in apps:
        label = tk.Label(myframe, text=app, bg="gray")
        label.pack()

# Runs all apps in the list.
def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg="#638EF9")
canvas.pack()

myframe = tk.Frame(root, bg="white")
myframe.place(relwidth=.8, relheight=.8, relx=.1, rely=.05)


h = Scrollbar(myframe, orient='horizontal')
v = Scrollbar(myframe)

h.pack(side = BOTTOM, fill = X)
v.pack(side = RIGHT, fill = Y)

openFile = tk.Button(root, text="Open File",
                     padx=10, pady=5,
                     fg="white", bg="#638EF9", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps",
                     padx=10, pady=5,
                     fg="white", bg="#638EF9", command=runApps)
runApps.pack()

# Create a label showing the directory for each app added.
for app in apps:
    label = tk.Label(myframe, text=app)
    label.pack()

root.mainloop()

with open('Saved Apps.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')




