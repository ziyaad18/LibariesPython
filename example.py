from tkinter import *


def build_gui():
    root = Tk()
    root.title("Adding Two Numbers")
    root.geometry("450x250")

    first_frame = Frame(root)
    first_frame.pack()

    second_frame = Frame(root)
    second_frame.pack()

    third_frame = Frame(root)
    third_frame.pack()

    fouth_frame = Frame(root)
    fouth_frame.pack()

    num_1 = IntVar()
    num_2 = IntVar()
    num_3 = IntVar()

    first_num_label = Label(first_frame, text="Please enter first number", padx="21", pady="20")
    first_num_label.pack(side=LEFT)

    first_num_entry = Entry(first_frame, textvariable=num_1)
    first_num_entry.pack(side=RIGHT)

    second_num_label = Label(second_frame, text="Please enter second number", padx="10", pady="20")
    second_num_label.pack(side=LEFT)

    second_num_entry = Entry(second_frame, textvariable=num_2)
    second_num_entry.pack(side=RIGHT)

    third_num_label = Label(third_frame, text="You answer", padx='65')
    third_num_label.pack(side=LEFT)

    third_num_entry = Entry(third_frame, textvariable=num_3)
    third_num_entry.pack(side=LEFT)

    def add_numbers():
        third_num_entry.insert(0, num_1.get() + num_2.get())

    add_btn = Button(text="Add", command=add_numbers)
    add_btn.pack(side=LEFT)

    def clear_all_num():
        first_num_entry.delete(0, END)
        second_num_entry.delete(0, END)
        third_num_entry.delete(0, END)

    clear_btn = Button(text="Clear", command=clear_all_num)
    clear_btn.pack(side=LEFT)

    def exit_program():
        root.destroy()

    exit_btn = Button(text="Exit", command=exit_program)
    exit_btn.pack(side=LEFT)

    root.mainloop()


build_gui()