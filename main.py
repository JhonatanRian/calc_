from tkinter import *

class calc:
    
    def __init__(self: object) -> None:
        self.window: Tk = Tk()
        self.window.title("Calc")
        self.window.resizable(0, 0)
        
        self.screen_number = Entry(self.window, font="arial 20 bold", bg="#25574b", fg="white", width=21)
        self.screen_number.pack()
        
        self.frame = Frame(self.window)
        self.frame.pack()
        
        self.button_1 = Button(self.frame, bg="orange", bd=0,text="1", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("1"))
        self.button_2 = Button(self.frame, bg="orange", bd=0,text="2", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("2"))
        self.button_3 = Button(self.frame, bg="orange", bd=0,text="3", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("3"))
        self.button_4 = Button(self.frame, bg="orange", bd=0,text="4", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("4"))
        self.button_5 = Button(self.frame, bg="orange", bd=0,text="5", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("5"))
        self.button_6 = Button(self.frame, bg="orange", bd=0,text="6", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("6"))
        self.button_7 = Button(self.frame, bg="orange", bd=0,text="7", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("7"))
        self.button_8 = Button(self.frame, bg="orange", bd=0,text="8", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("8"))
        self.button_9 = Button(self.frame, bg="orange", bd=0,text="9", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("9"))
        self.button_add = Button(self.frame, bg="orange", bd=0,text="+", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("+"))
        self.button_dimi = Button(self.frame, bg="orange", bd=0,text="-", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("-"))
        self.button_divi = Button(self.frame, bg="orange", bd=0,text="/", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("/"))
        self.button_mult = Button(self.frame, bg="orange", bd=0,text="x", font="arial 25 bold",
                               width=2, height=1, command=lambda: self.click("*"))
        self.button_equal = Button(self.frame, bg="orange", bd=0,text="=", font="arial 25 bold",
                               width=2, height=1, command=self.total)
        self.button_clean = Button(self.frame, bg="orange", bd=0,text="C", font="arial 25 bold",
                               width=2, height=1, command=self.Clean)
        
        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_add.grid(row=0, column=3)
        self.button_dimi.grid(row=1, column=3)
        self.button_divi.grid(row=2, column=3)
        self.button_mult.grid(row=0, column=4)
        self.button_clean.grid(row=1, column=4)
        self.button_equal.grid(row=2, column=4)
        
        
        self.window.mainloop()
        
    def click(self, num):
        self.screen_number.insert(END, num)
        
    def Clean(self):
        self.screen_number.delete(0, END)
        
    def total(self):
        try:
            resu = eval(self.screen_number.get())
            self.screen_number.delete(0, END)
            self.screen_number.insert(0, str(resu))
        except:
            self.screen_number.delete(0, END)
            self.screen_number.insert(0, "Não é possivel calcular")

calc()