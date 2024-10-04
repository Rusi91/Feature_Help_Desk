from tkinter import *
from Config import Config
from classes.HelpDesk import HelpDesk
from classes.MainApp import MainApp

import customtkinter


main_app = MainApp()
main_app.set_appearance(Config.MODE_COLOR, Config.DEFAULT_THEME_COLOR)
main_app.set_title(Config.TITLE)



def input():
    popupwindow = customtkinter.CTkToplevel(main_app.root)
    dialog = customtkinter.CTkInputDialog(popupwindow, text="What is your name?", title="kdjfkdfj")
    dialog2 = customtkinter.CTkInputDialog(popupwindow, text="What is your name?", title="kdjfkdfj")
    


test_btn = customtkinter.CTkButton(main_app.root, text=Config.TEST_BTN_TEXT, command=input)
test_btn.pack(pady=40)

main_app.loop()