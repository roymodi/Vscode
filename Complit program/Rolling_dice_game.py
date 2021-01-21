from tkinter import*
import random as rd

win=Tk()
win.title("Rolling dice")

photo_1=PhotoImage(file='C:/Users/bidyut/Downloads/images/dice1.png')
photo_2=PhotoImage(file='C:/Users/bidyut/Downloads/images/dice2.png')
photo_3=PhotoImage(file='C:/Users/bidyut/Downloads/images/dice3.png')
photo_4=PhotoImage(file='C:/Users/bidyut/Downloads/images/dice4.png')
photo_5=PhotoImage(file='C:/Users/bidyut/Downloads/images/dice5.png')
photo_6=PhotoImage(file='C:/Users/bidyut/Downloads/images/dice6.png')

imglist=[photo_1,photo_2,photo_3,photo_4,photo_5,photo_6]

imgshow=Label(win,image=photo_6)
imgshow.grid(row=0,column=1)

def click():
    global imgshow
    imgshow.grid_forget()
    rand=rd.randint(0,5)
    imgshow=Label(win,image=imglist[rand])
    imgshow.grid(row=0,column=1)


click=Button(win,text='Rolling Dice',padx=15,pady=2,command=click,activebackground="green",bg='pink')
click.grid(row=0,column=0)


win.mainloop()