from tkinter import*

w=Tk()
w.title('True & False')

e=Entry(w,width=5)
e.grid(row=0,column=1)

def fun():
    y=e.get()
    x=int(y)
    if x%2==0:
        true()
    else:
        false()
    e.delete(0,END)
    


def true():
    l=Label(w,text="True")
    l.grid(row=0,column=2)

def false():
    l=Label(w,text="False")
    l.grid(row=0,column=2)


b=Button(w,text='enter',command=fun)
b.grid(row=0,column=0)


w.mainloop()