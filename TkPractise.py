from tkinter import *
window = Tk()

window.title("calculator")
window.geometry("550x300")
window.configure(background="light blue")

frame1= Frame(window)
frame1.pack()

frame2= Frame(window)
frame2.pack()

frame3= Frame(window)
frame3.pack()

value_1=IntVar()
value_2=IntVar()
value_3=IntVar()

num1_label = Label(frame1, text="first number" , width="30", height="3")
num1_label.pack(side=LEFT)
num1_entry= Entry(frame1, textvariable=value_1)
num1_entry.pack(side=RIGHT)

num2_label = Label(frame2, text="second number", width="30", height="3")
num2_label.pack(side=LEFT)
num2_entry = Entry(frame2, textvariable=value_2)
num2_entry.pack(side=RIGHT)

num3_label = Label(frame3, text="result", width="30", height="3",)
num3_label.pack(side=LEFT)
num3_entry = Entry(frame3, textvariable=value_3)
num3_entry.pack(side=RIGHT)

def add():
    num3_entry.insert(0, value_1.get() + value_2.get())
    return None

button_add= Button(text="add", command=add,)
button_add.pack(side=LEFT)


def clear():
    num1_entry.delete(0, END)
    num2_entry.delete(0, END)
    num3_entry.delete(0, END)
    return None
button_clear = Button(text="Clear", command=clear)
button_clear.pack(side=LEFT)





window.mainloop()

