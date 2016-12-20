from tkinter import *
from PIL import Image, ImageTk

class TkInterEx:

    @staticmethod
    def quit_app(event=None):
        root.quit();

    def __init__(self, root: Tk):

        root.title("Toolbar Example")

        menubar = Menu(root)

        file_menu = Menu(root, tearoff = 0)

        file_menu.add_command(label="Open")

#https://youtu.be/AYOs78NjYfc?t=2m59s



