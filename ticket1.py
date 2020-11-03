# Import libraries
from tkinter import *
from tkinter import ttk

window = Tk()

window.title("Easy ticket")
3window.geometry("500x400")
window.configure(background="orange")

# Creates variables for prices
ssoccer = 30
movie = 50
theater = 150

# Creates Tkinter widgets
ticketvar = StringVar()

cellnum = Entry(window, width=20)
tickets = ttk.Combobox(window, textvariable=ticketvar, width=20, value=["Soccer", "Movie", "Theater"])
numbertik = ttk.Spinbox(window, from_=0, to=20, state="readonly")
celllabel = Label(window, text="Cellphone number:")
ticketslab = Label(window, text="Ticket Category:")
numlabel = Label(window, text="Number of tickets:")
anslabel = Label(window)





#Creates class
class clsTiketSales:
    def __init__(self, cellnum, numlabel, price):
        self.cellnum = cellnum
        self.numbertik = numbertik
        self.price = price
        return

# Creates function for button
def calc():
# Passes through class
    tksale = clsTiketSales(cellnum.get(), float(numbertik.get()), tickets.get())

# Desicion tree
    if tickets.get() == "Soccer":
        scprice = ssoccer * int(numbertik.get()) + (14/100)
        anslabel.config(text="Price:"+ str(scprice) + "\n" + "tickets:"+str(numbertik.get()) + "\n" +"Number:"+ str(cellnum.get()))
    if tickets.get() == "Movie":
        mvprice = movie * int(numbertik.get()) + (14/100)
        anslabel.config(text="Price:"+ str(mvprice) + "\n" + "tickets:"+str(numbertik.get()) + "\n" +"Number:"+ str(cellnum.get()))
    if tickets.get() == "Theater":
        thprice = theater * int(numbertik.get()) + (14/100)
        anslabel.config(text="Price:"+ str(thprice) + "\n" + "tickets:"+str(numbertik.get()) + "\n" +"Number:"+ str(cellnum.get()))


def clear():
    cellnum.delete('0', END)
    tickets.delete('0',END)
    numbertik.delete('0',END)

clearButton = Button (window, text = "Clear", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER,  overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = clear)
clearButton.grid(row = 8, column = 3,ipady = 8, ipadx = 12, pady = 5, sticky = NW)

#Creates button
tkbtn = Button(window, text="calculate", command=calc, width=20, height=1, font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, activeforeground="blue")
tkbtn.grid(row=8, column=0,ipady = 8, ipadx = 12, pady = 5, sticky = NW)
# Adds widgets
celllabel.grid(row=0, column=0, sticky=W)
cellnum.grid(row = 0, column=2)

tickets.grid(row=2, column=0, sticky=W)
tickets.grid(row=2, column=2)

numlabel.grid(row=4, column=0, sticky=W)
numbertik.grid(row=4, column=2)

anslabel.grid(row=6, column=0)



window.mainloop()