from tkinter import *

window= Tk()
window.title("bubble sort")
window.geometry("450x500")

def bubble(list2):

    for i in range(0, len(list2) - 1):
        for j in range(len(list2) - 1):
            if (list2[j] > list2[j + 1]):
                temp = list2[j]
                list2[j] = list2[j + 1]
                list2[j + 1] = temp

    return list2


list2 = ["tom", "ryan", "sam", "chloe", "nadine", "harry","jack","mike","ned","ben"]
print("The unsorted list is: ", list2)

print("The sorted list is: ", bubble(list2))




calculate_btn = Button(window, text="calculate", command=bubble(list2))
calculate_btn.grid(row=3, column=1)

output_label1 = Label(window,  bg="light blue", width="10", height="3",)
output_label1.grid(row=3, column=0)

















window.mainloop()


