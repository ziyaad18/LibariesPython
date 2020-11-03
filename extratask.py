from tkinter import *
# exam No 232423423532

window = Tk()

window.title("consultation fee")
window.geometry("550x300")



label1 = Label(window, text="SicknessCode" , width="30", height="3")
label1.grid(row=0, column=0)
box1=Entry(window)
box1.grid(row=0, column=1)

label2 = Label(window, text="DurationOfTreatment", width="30", height="3")
label2.grid(row=2, column=0)
box2 = Entry(window)
box2.grid(row=2, column=1)
label3 = Label(window, text="Weeks/Months")
label3.grid(row=2, column=3)

label4 = Label(window, text="DoctorsPractiseNUmber",  width="30", height="3")
label4.grid(row=3, column= 0)
box3 = Entry(window)
box3.grid(row=3, column=1)

label5 = Label(window, text="Scan/Consultation Fee")
label5.grid(row=4, column=0)
box4 = Entry(window)
box4.grid(row=4, column=1)


option = StringVar
R1 = Radiobutton(window, text="cancer", value="cancer", var=option)
R2 = Radiobutton(window, text="influenza",value="influenza", var=option )
R1.grid(row=5, column=1)
R2.grid(row=6, column=1)


label6= Label( window, text="AmountPaidForTreatment ", width="30", height="3")
label6.grid(row=7, column=0)








calcbtn = Button(window, )









window.mainloop()
