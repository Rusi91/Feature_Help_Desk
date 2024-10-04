from tkinter import *
from Config import Config

import customtkinter
import pyautogui

class HelpDesk:

    # später nur noch default init da root nicht mehr notwendig
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry(self.get_screen_resolution())
        

    def set_appearance(self, mode_color:str, theme_color:str):
        customtkinter.set_appearance_mode(mode_color)
        customtkinter.set_default_color_theme(theme_color)

    def set_title(self, title:str):
        self.root.title(title)

    def get_screen_resolution(self):
        screen_resolution = pyautogui.size()
        resolution_str = str(screen_resolution.width) + "x" + str(screen_resolution.width)
        return resolution_str
    
    def loop(self):
        self.root.mainloop()