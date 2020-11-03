from tkinter import *

root = Tk()

root.title('text file')
root.geometry('500x250')
root.configure(background='navy')

def createfile():
    file = open('/home/user/my_weekend_activities.txt','w+')
    file.write("We went to our cousins house\n")
    file.write("Had a lekka braai\n")
    file.write("Spend time with our family\n")
    file.write("Had a gaming tournament online whole night\n")
    file.close()




weekact = Label(root, text="My Weekend Activites").place(x="5", y="10")
widget = Text(root, height=6, width=55)
widget.pack(pady=40)


create = Button(root, text="Create File",command=createfile).place(x="5", y="175")

def textshow():
    text_file = open('/home/user/Desktop/my_weekend_activities.txt','r')
    text1=text_file.read()
    widget.insert(END,text1)
    text_file.close()

display = Button(root, text="Display", command=textshow).place(x="125", y="175")


def clear():
    widget.delete('1.0','end')



clr = Button(root, text="Clear",command=clear).place(x="225", y="175")


def exit():
    sys.exit()
close = Button(root, text="Exit",command=exit).place(x="310", y="175")

def append():
    with open("my_weekend_activities.txt", "a") as myfile:
        myfile.write("this is extrat ext\n")
        myfile.write("Second Line\n")

apend = Button(root, text="Append Data", command=append).place(x="385", y="175")




root.mainloop()

