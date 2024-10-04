from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from openpyxl import Workbook

import tkinter as tk
import openpyxl, xlrd
import pathlib

root = Tk()
root.title("Data Entry")
root.geometry("700x400")
root.resizable(False,False)
root.configure(bg="#326273")

# Heading
Label(root, text="Please fill out this Entry form: ", font="arial 13", bg="#326273", fg="#fff").place(x=20, y=20)

# label
Label(root, text="Name", font=23, bg="#326273", fg="#fff").place(x=50, y=100)
Label(root, text="Email", font=23, bg="#326273", fg="#fff").place(x=50, y=150)
Label(root, text="Maschine", font=23, bg="#326273", fg="#fff").place(x=50, y=200)
Label(root, text="Dringlichkeit", font=23, bg="#326273", fg="#fff").place(x=380, y=200)
Label(root, text="Nachricht", font=23, bg="#326273", fg="#fff").place(x=50, y=250)


#Entry
name_val = StringVar()
contact_val = StringVar()
machine_val = StringVar()

name_entry = Entry(root, textvariable=name_val, width=25, bd=2, font=20)
contact_entry = Entry(root, textvariable=contact_val, width=25, bd=2, font=20)
machine_entry = Entry(root, textvariable=machine_val, width=18, bd=2, font=20)

# priority
priority_combobox = Combobox(root, values=["Kritisch", "Hoch", "Normal", "Niedrig"], font="arial 14", state="r", width=14)
priority_combobox.place(x=500, y=200)
priority_combobox.set("Normal")

message_entry = Text(root, width=60, height=7, bd=2)

name_entry.place(x=150, y=100)
contact_entry.place(x=150, y=150)
machine_entry.place(x=150,y=200)
message_entry.place(x=150, y=250)



root.mainloop()
