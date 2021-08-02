from tkinter import *

class calc:
    
    def __init__(self: object) -> None:
        self.window: Tk = Tk()
        self.window.title("Calc")
        self.window.resizable(0, 0)
        self.window.config(bg="#25574b")
        self.frame: Frame = Frame(self.window, width=360, height=360, bg="#25574b")
        
        self.window.mainloop()

calc()