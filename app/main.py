from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox, PhotoImage
from openpyxl import Workbook
from PIL import ImageTk, Image
from Config import Config



import tkinter as tk
import openpyxl, xlrd
import pathlib

root = Tk()
root.title("DM & IIoT")
root.geometry("700x450")
root.resizable(False,False)
root.configure(bg="#326273")

#icon
icon_image = PhotoImage(file=Config.ICON_IMAGE)
root.iconphoto(False, icon_image)

def clear():
    name_val.set("")
    contact_val.set("")
    machine_val.set("")
    message_entry.delete(1.0, END)

def exit():
    root.destroy()

def submit():
    pass

# Heading
Label(root, text="Nachricht an das Team MD & IIoT", font="arial 20", bg="#326273", fg="#fff").place(x=20, y=20)

# label
Label(root, text="Name", font=23, bg="#326273", fg="#fff").place(x=50, y=100)
Label(root, text="Email", font=23, bg="#326273", fg="#fff").place(x=50, y=150)
Label(root, text="Maschine", font=23, bg="#326273", fg="#fff").place(x=50, y=200)
Label(root, text="Dringlichkeit", font=23, bg="#326273", fg="#fff").place(x=380, y=200)
Label(root, text="Nachricht", font=23, bg="#326273", fg="#fff").place(x=50, y=250)

image = Image.open(Config.TEST_IMAGE).resize((221,150))
photo = ImageTk.PhotoImage(image)


Label(root, image=photo).place(x=450,y=25)

#Entry
name_val = StringVar()
contact_val = StringVar()
machine_val = StringVar()

name_entry = Entry(root, textvariable=name_val, width=25, bd=2, font=1)
contact_entry = Entry(root, textvariable=contact_val, width=25, bd=2, font=2)
machine_entry = Entry(root, textvariable=machine_val, width=18, bd=2, font=2)

# priority
priority_combobox = Combobox(root, values=["Kritisch", "Hoch", "Normal", "Niedrig"], font="arial 14", state="r", width=14)
priority_combobox.place(x=500, y=200)
priority_combobox.set("Normal")

message_entry = Text(root, width=65, height=7, bd=2)

name_entry.place(x=150, y=100)
contact_entry.place(x=150, y=150)
machine_entry.place(x=150,y=200)
message_entry.place(x=150, y=250)

Button(root, text="Senden", bg="#326273", fg="white", width=15, height=2).place(x=150,y=380)
Button(root, text="Löschen", bg="#326273", fg="white", width=15, height=2).place(x=350,y=380)
Button(root, text="Abbrechen", bg="#326273", fg="white", width=15, height=2, command=exit).place(x=560,y=380)

root.mainloop()
