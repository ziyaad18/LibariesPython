from tkinter import *
import tkinter


window = Tk()
window.geometry("200x250")
window.title("Register")
window.configure(background="grey")

fields = {}
#name
name_label = Label(window, text="Name")
name_field = Entry(window)
fields["name"] = name_field
name_label.grid(row=0, column=0)
name_field.grid(row=0, column=1)
# surname
surname_label =Label(window, text="Surname")
surname_field =Entry(window)
fields["surname"] = surname_field
surname_label.grid(row=1, column=0)
surname_field.grid(row=1, column=1)



#email
email_label = Label(window, text="Email")
email_field= Entry(window)
fields["email"] = email_field

email_label.grid(row=2, column=0)
email_field.grid(row=2, column=1)
#number
number_label = Label(window, text= "number")
number_field = Entry(window)
fields["number"] = number_field


number_label.grid(row=3, column=0)
number_field.grid(row=3, column=1)
#contact
contact_label = Label(window, text="contact")
contact_field = Entry(window)
fields["'contact"] = contact_field

contact_label.grid(row=4, column=0)
contact_field.grid(row=4, column=1)
def submit_command():
    output = "User data:\n"
    for key in fields.keys():
        output +=f"{key}: {fields[key].get()}\n"
    print(output)







submit = Button(window, text=" submit", command=submit_command)
submit.grid(row=5, column=0)



window.mainloop()