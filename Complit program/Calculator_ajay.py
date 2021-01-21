from tkinter import*

class Calculator:

    def getinput(self):
        self.userinput=self.entry.get()

    def clearinput(self):
        self.entry.delete(0,END)

    def root(self):         # root funtion (input number ** 0.5)
        self.getinput()        # call userinput funtion
        num=self.userinput  # self.userinput is str
        no=float(num)         # self.userinput convert to float

        try:
            self.result=no**0.5
        finally:
            self.entry.delete(0,END)
            self.entry.insert(0,self.result)

    def squar(self):      
        self.getinput()
        num=self.userinput
        no=float(num)
        try:
            self.result=no**2
        finally:
            self.entry.delete(0,END)
            self.entry.insert(0,self.result)


    def click(self,argv):
        self.entry.insert(END,argv)


    def equal(self):
        self.getinput()
        try:
            self.result=eval(self.userinput)
        except ZeroDivisionError:
            self.entry.delete(0,END)
            self.entry.insert(0,"Not a Number")
        except SyntaxError:
            self.entry.delete(0,END)
            self.entry.insert(0,"Input Error")
        else:
            self.entry.delete(0,END)
            self.entry.insert(0,self.result)

    def __init__(self, win):
        
        
        win.title("Calculator")
        win.geometry()
        win.resizable(False,False) # no resize window because it false

        self.entry=Entry(win,width=30,borderwidth=4,fg='blue',justify=RIGHT)
        self.entry.grid(row=0,column=0,columnspan=4,padx=20,pady=5,sticky=W+E)

        button_1=Button(win,text='1',padx=20,pady=5,borderwidth=3,bg='#ffffff',command=lambda:self.click('1'))
        button_2=Button(win,text='2',padx=20,pady=5,borderwidth=3,bg='#ffffff',command=lambda:self.click('2'))
        button_3=Button(win,text='3',padx=20,pady=5,borderwidth=3,bg='#ffffff',command=lambda:self.click('3'))
        button_4=Button(win,text='4',padx=20,pady=5,borderwidth=3,bg='#ffffff',command=lambda:self.click('4'))
        button_5=Button(win,text='5',padx=20,pady=5,borderwidth=3,bg='#ffffff',command=lambda:self.click('5'))
        button_6=Button(win,text='6',padx=20,pady=5,borderwidth=3,bg='#ffffff',command=lambda:self.click('6'))
        button_7=Button(win,text='7',padx=20,pady=5,borderwidth=3,bg='#ffffff',command=lambda:self.click('7'))
        button_8=Button(win,text='8',padx=20,pady=5,borderwidth=3,bg='#ffffff',command=lambda:self.click('8'))
        button_9=Button(win,text='9',padx=20,pady=5,borderwidth=3,bg='#ffffff',command=lambda:self.click('9'))
        button_0=Button(win,text='0',padx=20,pady=5,borderwidth=3,bg='#ffffff',command=lambda:self.click('0'))
        button_decimal=Button(win,text='.',padx=21,pady=5,borderwidth=3,bg='#ffffff',command=lambda:self.click('.'))   
        button_add=Button(win,text='+',padx=20,pady=5,borderwidth=3,bg='#808080',command=lambda:self.click('+'))
        button_sub=Button(win,text='-',padx=20,pady=5,borderwidth=3,bg='#808080',command=lambda:self.click('-'))
        button_mult=Button(win,text='*',padx=20,pady=5,borderwidth=3,bg='#808080',command=lambda:self.click('*'))
        button_divi=Button(win,text='/',padx=20,pady=5,borderwidth=3,bg='#808080',command=lambda:self.click('/'))
        button_squar=Button(win,text='Squar',padx=20,pady=5,borderwidth=3,bg='#808080',command=lambda : self.squar())
        button_root=Button(win,text='Root',padx=20,pady=5,borderwidth=3,bg='#808080',command=lambda : self.root())
        
        button_equal=Button(win,text='=',padx=20,pady=5,borderwidth=3,bg='#808080',command=lambda:self.equal())
        button_clear=Button(win,text='C',padx=20,pady=5,borderwidth=3,bg='#808080',command=lambda:self.clearinput())
        button_modulas=Button(win,text='%',padx=20,pady=5,borderwidth=3,bg='#808080',command=lambda : self.click("%"))

        button_1.grid(row=4,column=0,sticky=W+E)
        button_2.grid(row=4,column=1,sticky=W+E)
        button_3.grid(row=4,column=2,sticky=W+E)
        button_4.grid(row=3,column=0,sticky=W+E)
        button_5.grid(row=3,column=1,sticky=W+E)
        button_6.grid(row=3,column=2,sticky=W+E)
        button_7.grid(row=2,column=0,sticky=W+E)
        button_8.grid(row=2,column=1,sticky=W+E)
        button_9.grid(row=2,column=2,sticky=W+E)
        button_0.grid(row=5,column=0,sticky=W+E)

        button_decimal.grid(row=5,column=1,sticky=W+E)
        button_equal.grid(row=5,column=2,sticky=W+E)
        button_add.grid(row=5,column=3,sticky=W+E)
        button_sub.grid(row=4,column=3,sticky=W+E)
        button_mult.grid(row=3,column=3,sticky=W+E)
        button_divi.grid(row=2,column=3,sticky=W+E)
        button_squar.grid(row=1,column=1,sticky=W+E)
        button_root.grid(row=1,column=2,sticky=W+E)
        button_clear.grid(row=1,column=3,sticky=W+E)
        button_modulas.grid(row=1,column=0,sticky=W+E)

win = Tk()
Calculator(win)
win.mainloop()