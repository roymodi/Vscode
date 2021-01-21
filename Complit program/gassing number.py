from tkinter import*
import random

w=Tk()
w.title('Gaussing Number')

no=random.randint(1,101)

lab=Label(w,text="Gassing number\n(1,100): ")
lab.grid(row=0,column=0)

e=Entry(w,width=5)
e.grid(row=0,column=1)

l=Label(w,text='Play')
l.grid(row=1,column=1)

def game():
    y=e.get()
    x=int(y)
    if x==no:
        win()
    if x>no:
        high()
    if x<no:
        low()


def win():
    global l
    l.grid_forget()
    l=Label(w,text="Win",fg='green',font='bold')
    l.grid(row=1,column=1)

def low():
    global l
    e.delete(0,END)
    l.grid_forget()
    l=Label(w,text='Too Low',fg='red')
    l.grid(row=1,column=1)

def high():
    global l
    e.delete(0,END)
    l.grid_forget()
    l=Label(w,text='Too High',fg='blue')
    l.grid(row=1,column=1)


b=Button(w,text='Play',command=game,width=10)
b.grid(row=1,column=0,sticky=W)


w.mainloop()