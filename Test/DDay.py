from tkinter import *

class D_day:
    def __init__(self, root):
        self.root = root
        self.root.geometry('100x110+350+70')
        button1 = Checkbutton(self.root, text='Very High', command=self.callback)
        button2 = Checkbutton(self.root, text='Very High')
        button3 = Checkbutton(self.root, text='High')
        button4 = Checkbutton(self.root, text='Normal')
        button5 = Checkbutton(self.root, text='Low')
        button1.pack(side="top")
        button2.pack(side="top")
        button3.pack(side="top")
        button4.pack(side="top")
        button5.pack(side="top")
        button1.selection_get()

    def callback(self):
        print ("You clicked me!\n")

root = Tk()
root.title("D Day Test")
d_day = D_day(root)
root.mainloop()