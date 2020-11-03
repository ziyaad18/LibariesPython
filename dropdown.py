from tkinter import *

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

Window = Tk()

variable = StringVar(Window)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(Window, variable, *OPTIONS)
w.grid(row=1, column=3)


mainloop()
