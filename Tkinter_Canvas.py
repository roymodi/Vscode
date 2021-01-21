from tkinter import*
win=Tk()


canvas=Canvas(height=250,width=300)
canvas.pack()
canvas.create_line(100,0,100,100)


win.mainloop()