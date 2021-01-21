from tkinter import*

root=Tk()
root.title('image_changer')

photo_1=PhotoImage(file='C:/Users/bidyut/Downloads/images/dice1.png')
photo_2=PhotoImage(file='C:/Users/bidyut/Downloads/images/dice2.png')
photo_3=PhotoImage(file='C:/Users/bidyut/Downloads/images/dice3.png')
photo_4=PhotoImage(file='C:/Users/bidyut/Downloads/images/dice4.png')
photo_5=PhotoImage(file='C:/Users/bidyut/Downloads/images/dice5.png')
photo_6=PhotoImage(file='C:/Users/bidyut/Downloads/images/dice6.png')


imglist=[photo_1,photo_2,photo_3,photo_4,photo_5,photo_6]

imgshow=Label(root,image=photo_1)
imgshow.grid(row=0,column=0,columnspan=3)
status=Label(root,text='image no: 1',bd=2,bg='pink',relief=SUNKEN)
status.grid(row=2,column=0,columnspan=2)

def forward(no):
    global imgshow
    global b_back
    global b_forward

    imgshow.grid_forget()
    imgshow=Label(root,image=imglist[no-1])
    b_forward=Button(root,text='>>',command=lambda:forward(no+1))
    b_back=Button(root,text='<<',command=lambda :back(no-1))
    status=Label(root,text='image no:'+str(no),bd=2,bg='pink',relief=SUNKEN)

    if no==6:
        b_forward=Button(root,text='>>',state=DISABLED)

    
    
    b_back.grid(row=1,column=0)
    b_forward.grid(row=1,column=2)
    imgshow.grid(row=0,column=0,columnspan=3)
    status.grid(row=2,column=0,columnspan=2)

def back(no):
    global imgshow
    global b_back
    global b_forward

    imgshow.grid_forget()
    imgshow=Label(root,image=imglist[no-1])
    b_forward=Button(root,text='>>',command=lambda:forward(no+1))
    b_back=Button(root,text='<<',command=lambda :back(no-1))
    status=Label(root,text='image no:'+str(no),bd=2,bg='pink',relief=SUNKEN)

    if no==1:
        b_back=Button(root,text='<<',command=back,state=DISABLED)

    b_back.grid(row=1,column=0)
    b_forward.grid(row=1,column=2)
    imgshow.grid(row=0,column=0,columnspan=3)
    status.grid(row=2,column=0,columnspan=2)



b_back=Button(root,text='<<',command=back,state=DISABLED)
b_exit=Button(root,text='Exit',command=root.quit)
b_forward=Button(root,text='>>',command=lambda:forward(2))

b_back.grid(row=1,column=0)
b_exit.grid(row=1,column=1)
b_forward.grid(row=1,column=2)

root.mainloop()