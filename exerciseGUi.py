from tkinter import *


def build_program():
    window = Tk()
    window.title("Adding Two Numbers")
    window.geometry("500x250")

    frame_1 = Frame(window)
    frame_1.pack()
    frame_2 = Frame(window)
    frame_2.pack()
    frame_3 = Frame(window)
    frame_3.pack()

    num_value_1 = IntVar()
    num_value_2 = IntVar()
    num_value_3 = IntVar()

    first_num_label = Label(frame_1, text="Please enter first number", padx="21", pady="20")
    first_num_label.pack(side=LEFT)
    first_num_entry = Entry(frame_1, textvariable=num_value_1)
    first_num_entry.pack(side=RIGHT)

    second_num_label = Label(frame_2, text="Please enter second number", padx="10", pady="20")
    second_num_label.pack(side=LEFT)
    second_num_entry = Entry(frame_2, textvariable=num_value_2)
    second_num_entry.pack(side=RIGHT)

    third_num_label = Label(frame_3, text="Your answer", padx='65')
    third_num_label.pack(side=LEFT)
    third_num_entry = Entry(frame_3, textvariable=num_value_3)
    third_num_entry.pack(side=LEFT)

    def plus():
        third_num_entry.insert(0, num_value_1.get() + num_value_2.get())

    add_button = Button(text="Add", command=plus)
    add_button.pack(side=LEFT)

    def clear_all():
        first_num_entry.delete(0, END)
        second_num_entry.delete(0, END)
        third_num_entry.delete(0, END)

    clear_button = Button(text="Clear", command=clear_all)
    clear_button.pack(side=LEFT)

    def finish_program():
        window.destroy()

    exit_button = Button(text="Exit", command=finish_program)
    exit_button.pack(side=LEFT)

    window.mainloop()


build_program()


































