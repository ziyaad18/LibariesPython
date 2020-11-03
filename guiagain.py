from tkinter import *
def test():
    mytext ="fortnite"
    messagebox.insert(0, mytext)
    return None

frame = Tk()

frame.title("Program")

frame.geometry("550x300")

frame.configure(background="blue")


button = Button(frame, text="click ", bg="red", command=test)
messagebox = Entry(frame, width="30")
theLabel = Label(frame, text="hello everyone", relief="solid", font="bold")

theLabel.pack()
button.pack()
messagebox.pack()

frame.mainloop()



