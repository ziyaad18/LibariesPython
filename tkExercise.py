from tkinter import *
import tkinter
from tkinter import messagebox

top = tkinter.Tk()

top.geometry("400x400")

def display_superheroes():
    output = "Superheroes:"
    if CheckVar1.get(): # if Spiderman
        output += "\n you selected Spiderman."

    if CheckVar2.get(): # if Batman
        output += "\n you selected Batman"

    if CheckVar3.get(): # if Ironman
        output += "\n you selected Ironman"

    messagebox.showinfo("Superheroes", output)

B1 = tkinter.Button(top, text= "Show superheroes", command=display_superheroes)

CheckVar1 = BooleanVar()
CheckVar2= BooleanVar()
CheckVar3= BooleanVar()

CB1 = tkinter.Checkbutton(top, text="Spiderman", variable=CheckVar1, onvalue=True, offvalue=False, height=5, width=20)
CB2 = tkinter.Checkbutton(top, text="Batman", variable=CheckVar2, onvalue=True, offvalue=False, height=5, width=20)
CB3 = tkinter.Checkbutton(top, text="Ironman", variable=CheckVar3, onvalue=True, offvalue=False, height=5, width=20)

CB1.pack()
CB2.pack()
CB3.pack()
B1.pack()

top.mainloop()