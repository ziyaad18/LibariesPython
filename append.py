file = open('/home/user/Desktop/bozzafriday.txt','w+')
file.write("i am crazy\n")
file.write("i want a good meal\n")
file.write("ps4\n")
file.close()

file = open('/home/user/Desktop/bozzafriday.txt','r')
for each in file:
    print(each)