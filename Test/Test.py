from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self = Tk()
        self.geometry('100x110+350+70')
        button1 = Checkbutton(self, text='Very High', command=self.callback)
        button2 = Checkbutton(self, text='Very High')
        button3 = Checkbutton(self, text='High')
        button4 = Checkbutton(self, text='Normal')
        button5 = Checkbutton(self, text='Low')
        button1.pack(side="top")
        button2.pack(side="top")
        button3.pack(side="top")
        button4.pack(side="top")
        button5.pack(side="top")

    def callback(self):
        print("clicked!")


root = Tk()
app = Application(master=root)
app.mainloop()
