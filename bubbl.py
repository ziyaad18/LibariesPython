#def bubbles(list1):
   # n=len(list1)
    #for x in range(n):
      #  for i in range(0,n-x-1):
          #  if (list1[i]>list1[i+n]):
               # list1[i],list1[i+n]=list1()



def bubble(names):

    for i in range(0, len(names) - 1):
        for j in range(len(names) - 1):
            if (names[j] > names[j + 1]):
                temp = names[j]
                names[j] = names[j + 1]
                names[j + 1] = temp
    return names


names = ["tom", "ryan", "sam", "chloe", "nadine", "harry","jack","mike","ned","ben"]
print("The unsorted list is: ", names)

print("The sorted list is: ", bubble(names))











