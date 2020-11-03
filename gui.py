
import tkinter


from tkinter import messagebox

from tkinter import Canvas

top = tkinter.Tk()

top.geometry('100x100')

def hello():
    tkinter.messagebox.showinfo("say hello cat ", "hello cat world")




B1 = tkinter.Button(top, text="say hello cat ", command=hello)
B1.place(x=35, y=50)
w = Canvas(top, bd=4,bg="red", cursor="circle", width=100, height=100)
coord = 10, 50, 240, 210
w.create_arc(coord, start =0, extent =150, fill= "blue")
w.pack()


Checkvar1 =Intvar()
CheckVar2 =Intvar()

CB1 = tkinter.CHECKBUTTON(top, text="dog", variable=Checkvar1, onvalue=1, offvalue=0, height=5, width=20)
CB2 = tkinter.Checkbutton(top,text="cat", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20)

CB1.pack()
CB2.pack()




top.mainloop()
# make a window with a checkbox and a button
# when the button is clicked show if it was selected





