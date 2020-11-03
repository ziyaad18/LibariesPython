from tkinter import *# import everything
import tkinter
from tkinter import messagebox

top = Tk()# window
top.title("Choose your pet")
top.geometry("300x200")#size of screen
top.configure(background="grey")

def submit_command():
    info = "your choosen pets:\n"
    if dog_var.get():
        info += "you choose a dog\n"
    if cat_var.get():
            info += "you choose a cat\n"
    if bird_var.get():
        info += "you choose a bird\n"
    if info == "your choosen pets:\n":
        info = "you chose nothing"
    messagebox.showinfo("choose pets", info)

submit_button = Button(top, text="Submit", command=submit_command)


dog_var = BooleanVar()#get info from checkbutton
cat_var = BooleanVar()#
bird_var = BooleanVar()

dog_cb = Checkbutton(top, text="Dog", variable=dog_var, onvalue=True, offvalue=False, height=2, width=20)
cat_cb = Checkbutton(top, text="cat", variable=cat_var, onvalue=True, offvalue=False, height=2, width=20)
bird_cb = Checkbutton(top, text="bird", variable=bird_var, onvalue=True, offvalue=False, height=2, width=20)

dog_cb.pack()
cat_cb.pack()
bird_cb.pack()
submit_button.pack()





top.mainloop()# run function
