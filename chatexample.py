from tkinter import *        
win= Tk()

def read(val):
    ke=val
    file_r=open('chat_bot\\data\\data.txt','r')
    file=file_r.readlines()
    for x in file:
        re=x.replace('\n','')
        lis=re.split(':')
        key=lis[0]
        valu=lis[1]
        value=valu.capitalize()
        if ke in key:
            return value
        else:
            return False
        file_r.close()

def send():
    msg=entry.get()
    entry.delete(0,END)
    text.config(state=NORMAL)
    text.insert(END,'You: '+msg+'\n')
    ans=read(msg)
    reply=str(ans)
    txt="#####__TechMe Please__#####"
    cen=txt.center(35)
    if ans==False:
        text.insert(END,cen+'\n\n')
    else:
        text.insert(END,"Bot: "+reply+'\n\n')

    text.config(state=DISABLED)



text=Text(win,height=25,width=35,bg='#99ff99',relief=GROOVE,state=DISABLED)
entry=Entry(win,width=23,borderwidth=0,bg='#f2f2f2',font='arial')
button=Button(win,command=send,text='Send',padx=8,pady=8,width=7,borderwidth=1,bg='#4dffff')

button.grid(row=1,column=1,sticky=E)
entry.grid(row=1,column=0,columnspan=1,sticky=W)
text.grid(row=0,column=0,columnspan=2)


win.mainloop()  