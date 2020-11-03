from tkinter import *
window = Tk()
window.title("TicketSales")
window.geometry("450x300")

def calculate():
    tksale = clsTiketSales(cellno.get(), float(num_ticket.get()), tickettype.get())

# Ticket type and Calculation #Added Vat
    if tickettype.get() == "Soccer":
        scprice = socceram * int(num_ticket.get()) + (socceram * int(num_ticket.get())*(14/100))
        anslbl.config(text="Price:"+ str(scprice) + "\n"+ ("(VAT included)") + "\n" + "Amount of Tickets:"+"\n" +str(num_ticket.get()) + "\n" +"Reservation done by:"+ str(cellno.get()))
    if tickettype.get() == "Movie":
        mvprice = movieam * int(num_ticket.get()) + (movieam * int(num_ticket.get()) *(14/100))
        anslbl.config(text="Price:"+ str(mvprice) + "\n" +("(VAT included)") + "\n" "Amount of Tickets:"+"\n" +str(num_ticket.get()) + "\n" +"Reservation done by:"+ str(cellno.get()))
    if tickettype.get() == "Theater":
        thprice = theateram * int(num_ticket.get()) + (theateram * int(num_ticket.get())*(14/100))
    anslbl.config(text="Price:"+ str(thprice) + "\n" +("(VAT included)") + "\n" "Amount of Tickets:"+"\n" +str(num_ticket.get()) + "\n" +"Reservation done by:"+ str(cellno.get()))


contactNo = Label(window, text="Enter Cell number:", )
contactNo.grid(row=0, column=0)
contactEnt = Entry(window)
contactEnt.grid(row=0, column=1)

category = Label(window, text="Select TicketCategory:",)
category.grid(row=1, column=0)



TicketsAvailable = [
"Soccer",
"Movie",
"Theater"
]



variable = StringVar(window)
variable.set(TicketsAvailable[0]) # default value

w = OptionMenu(window, variable, *TicketsAvailable)
w.grid(row=1, column=1)

def clear():
    contactEnt.delete(0,END)

calculate = Button(window, text="Calculate")
calculate.grid(row=2, column=0)

clear = Button(window, text="Clear Entries",command=clear) # i call the function but it wont run
clear.grid(row=2, column=1)

output_label1 = Label(window,  bg="light blue", width="10", height="3")
output_label1.grid(row=3, column=0)



























window.mainloop()