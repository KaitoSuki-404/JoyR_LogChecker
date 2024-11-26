import tkinter as tk
import tkinter.ttk


class GUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(False, False)

    def changeTitle(self, title:str):
        self.window.title(title)

    def changeSize(self, x:int, y:int):
        geometry = str(x) + "x" + str(y)
        self.window.geometry(geometry)

    def onLoop(self):
        self.window.mainloop()

