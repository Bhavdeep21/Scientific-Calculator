from tkinter import *
import math as f

class calculate():

    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")

        self.resultwindow = Entry(self.root)
        self.resultwindow.grid(row=0,column=0,columnspan=5)
        self.resultwindow.config(font=("Arial", 18))
        self.resultwindow.focus_set()


        self.button1 = Button(self.root, text="1", width=3, command=lambda:self.ins('1'))
        self.button1.grid(row=1,column=0, padx=3, pady=3)
        self.button1.config(font=("Arial", 18))

        self.button2 = Button(self.root, text="2", width=3, command=lambda:self.ins('2'))
        self.button2.grid(row=1, column=1, padx=3, pady=3)
        self.button2.config(font=("Arial", 18))

        self.button3 = Button(self.root, text="3", width=3, command=lambda:self.ins('3'))
        self.button3.grid(row=1, column=2, padx=3, pady=3)
        self.button3.config(font=("Arial", 18))

        self.button4 = Button(self.root, text="4", width=3, command=lambda:self.ins('4'))
        self.button4.grid(row=2, column=0, padx=3, pady=3)
        self.button4.config(font=("Arial", 18))

        self.button5 = Button(self.root, text="5", width=3, command=lambda:self.ins('5'))
        self.button5.grid(row=2, column=1, padx=3, pady=3)
        self.button5.config(font=("Arial", 18))

        self.button6 = Button(self.root, text="6", width=3, command=lambda:self.ins('6'))
        self.button6.grid(row=2, column=2, padx=3, pady=3)
        self.button6.config(font=("Arial", 18))

        self.button7 = Button(self.root, text="7", width=3, command=lambda:self.ins('7'))
        self.button7.grid(row=3, column=0, padx=3, pady=3)
        self.button7.config(font=("Arial", 18))

        self.button8 = Button(self.root, text="8", width=3, command=lambda:self.ins('8'))
        self.button8.grid(row=3, column=1, padx=3, pady=3)
        self.button8.config(font=("Arial", 18))

        self.button9 = Button(self.root, text="9", width=3, command=lambda:self.ins('9'))
        self.button9.grid(row=3, column=2, padx=3, pady=3)
        self.button9.config(font=("Arial", 18))

        self.button0 = Button(self.root, text="0", width=3, command=lambda: self.ins('0'))
        self.button0.grid(row=4, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button_open = Button(self.root, text="(", width=3, command=lambda: self.ins('('))
        self.button_open.grid(row=4, column=1, padx=3, pady=3)
        self.button_open.config(font=("Arial", 18))

        self.button_close = Button(self.root, text=")", width=3, command=lambda: self.ins(')'))
        self.button_close.grid(row=4, column=2, padx=3, pady=3)
        self.button_close.config(font=("Arial", 18))
        
        self.buttonp = Button(self.root, text=".", width=3, command=lambda: self.ins('.'))
        self.buttonp.grid(row=4, column=3, padx=3, pady=3)
        self.buttonp.config(font=("Arial", 18))
        
        self.buttonlog = Button(self.root, text="log", width=3, command=lambda:self.ins('f.log('))
        self.buttonlog.grid(row=1, column=5, padx=3, pady=3)
        self.buttonlog.config(font=("Arial", 18))
        
        self.buttonceil = Button(self.root, text="ceil", width=3, command=lambda:self.ins('f.ceil('))
        self.buttonceil.grid(row=1, column=6, padx=3, pady=3)
        self.buttonceil.config(font=("Arial", 18))
        
        self.buttonfloor = Button(self.root, text="floor", width=3, command=lambda:self.ins('f.floor('))
        self.buttonfloor.grid(row=1, column=7, padx=3, pady=3)
        self.buttonfloor.config(font=("Arial", 18))
        
        self.buttonsin = Button(self.root, text="sin", width=3, command=lambda:self.ins('f.sin('))
        self.buttonsin.grid(row=2, column=5, padx=3, pady=3)
        self.buttonsin.config(font=("Arial", 18))
        
        self.buttoncos = Button(self.root, text="cos", width=3, command=lambda:self.ins('f.cos('))
        self.buttoncos.grid(row=2, column=6, padx=3, pady=3)
        self.buttoncos.config(font=("Arial", 18))
        
        self.buttontan = Button(self.root, text="tan", width=3, command=lambda:self.ins('f.tan('))
        self.buttontan.grid(row=2, column=7, padx=3, pady=3)
        self.buttontan.config(font=("Arial", 18))
        
        self.button_asin = Button(self.root, text="asin", width=3, command=lambda:self.ins('f.asin('))
        self.button_asin.grid(row=3, column=5, padx=3, pady=3)
        self.button_asin.config(font=("Arial", 18))
        
        self.button_acos = Button(self.root, text="acos", width=3, command=lambda:self.ins('f.acos('))
        self.button_acos.grid(row=3, column=6, padx=3, pady=3)
        self.button_acos.config(font=("Arial", 18))
        
        self.button_atan = Button(self.root, text="atan", width=3, command=lambda:self.ins('f.atan('))
        self.button_atan.grid(row=3, column=7, padx=3, pady=3)
        self.button_atan.config(font=("Arial", 18))
        
        self.buttonsqrt = Button(self.root, text="sqrt", width=3, command=lambda:self.ins('f.sqrt('))
        self.buttonsqrt.grid(row=4, column=6, padx=3, pady=3)
        self.buttonsqrt.config(font=("Arial", 18))
        
        self.buttonsqr = Button(self.root, text="**", width=3, command=lambda:self.ins('**'))
        self.buttonsqr.grid(row=4, column=7, padx=3, pady=3)
        self.buttonsqr.config(font=("Arial", 18))
        
        self.buttonabs = Button(self.root, text="abs", width=3, command=lambda:self.ins('abs('))
        self.buttonabs.grid(row=0, column=5, padx=3, pady=3)
        self.buttonabs.config(font=("Arial", 18))
        
        self.buttonexp = Button(self.root, text="exp", width=3, command=lambda:self.ins('f.exp('))
        self.buttonexp.grid(row=0, column=6, padx=3, pady=3)
        self.buttonexp.config(font=("Arial", 18))
        
        self.buttonfldivide = Button(self.root, text="//", width=3, command=lambda:self.ins('//'))
        self.buttonfldivide.grid(row=0, column=7, padx=3, pady=3)
        self.buttonfldivide.config(font=("Arial", 18))

        self.buttonplus = Button(self.root, text="+", width=3, command=lambda:self.ins('+'))
        self.buttonplus.grid(row=1, column=3, padx=3, pady=3)
        self.buttonplus.config(font=("Arial", 18))

        self.buttonminus = Button(self.root, text="-", width=3, command=lambda:self.ins('-'))
        self.buttonminus.grid(row=1, column=4, padx=3, pady=3)
        self.buttonminus.config(font=("Arial", 18))

        self.buttondivide = Button(self.root, text="/", width=3, command=lambda:self.ins('/'))
        self.buttondivide.grid(row=2, column=3, padx=3, pady=3)
        self.buttondivide.config(font=("Arial", 18))

        self.buttonmultiply = Button(self.root, text="*", width=3, command=lambda:self.ins('*'))
        self.buttonmultiply.grid(row=2, column=4, padx=3, pady=3)
        self.buttonmultiply.config(font=("Arial", 18))

        self.buttoncancel = Button(self.root, text="C", width=3, command=lambda: self.cancel())
        self.buttoncancel.grid(row=3, column=4, padx=3, pady=3)
        self.buttoncancel.config(font=("Arial", 18))

        self.buttondeleteall = Button(self.root, text="Del", width=3, command=lambda: self.delete_all())
        self.buttondeleteall.grid(row=3, column=3, padx=3, pady=3)
        self.buttondeleteall.config(font=("Arial", 18))

        self.buttonresult = Button(self.root, text="=", width=6, command=lambda:self.calculate())
        self.buttonresult.grid(row=4, column=4, padx=3, pady=3, columnspan=2)
        self.buttonresult.config(font=("Arial", 18))

        self.root.mainloop()

    def ins(self,val):
        self.resultwindow.insert(END, val)

    def cancel(self):
        self.resultwindow.delete(0, 'end')

    def delete_all(self):
        x = self.resultwindow.get()
        self.resultwindow.delete(0, 'end')
        y = x[:-1]
        self.resultwindow.insert(0, y)

    def calculate(self):
        x = self.resultwindow.get()
        answer = eval(x)
        self.resultwindow.delete(0, 'end')
        self.resultwindow.insert(0, answer)


calculate()