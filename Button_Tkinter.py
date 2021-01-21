from tkinter import*
win=Tk()

b_1=Button(win,text="click")
b_1.grid(row=0,column=0)

b_2=Button(win,text="actbg",activebackground='green')
b_2.grid(row=1,column=0)

b_3=Button(win,text="actfg",activeforeground='red')
b_3.grid(row=3,column=0)

b_4=Button(win,text="bd=5",bd=5)
b_4.grid(row=4,column=0)

b_5=Button(win,text="yellow",bg='yellow')
b_5.grid(row=5,column=0)

b_6=Button(win,text="destroy",command=win.destroy)
b_6.grid(row=0,column=1)

b_7=Button(win,text="red",fg='red')
b_7.grid(row=0,column=2)

b_8=Button(win,text="font",font='Helvetica')
b_8.grid(row=0,column=3)

b_9=Button(win,text="height",height=3)
b_9.grid(row=0,column=4)

b_10=Button(win,text="highlightcolor",highlightcolor='green')
b_10.grid(row=1,column=1)

#photo=PhotoImage(file="C:/Users/bidyut/Vscode/dice1.png")

#b_11=Button(win,image=photo)
#b_11.grid(row=1,column=2)

b_12=Button(win,text='justify',justify=LEFT,padx=2,pady=3)
b_12.grid(row=1,column=3)

b_13=Button(win,text="relief",relief=GROOVE)
b_13.grid(row=1,column=4)
b_130=Button(win,text="relief",relief=SUNKEN)
b_130.grid(row=1,column=5)
b_13d=Button(win,text="relief",relief=RIDGE)
b_13d.grid(row=1,column=6)

b_12d=Button(win,text="state(disable)",state=DISABLED)
b_12d.grid(row=2,column=0)
b_1d2=Button(win,text="state(active)",state=ACTIVE)
b_1d2.grid(row=2,column=1)

b_14=Button(win,text="underline",underline=10,width=10)
b_14.grid(row=2,column=2)

b_154=Button(win,text="wraplength",wraplength=2)
b_154.grid(row=2,column=3)




win.mainloop()