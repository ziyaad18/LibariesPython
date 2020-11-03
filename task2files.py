import random
path=open('/home/user/Desktop/bozzafriday.txt','r')
line=path.readlines()
sentence=[]
for i in range(0,len(line)-1):
    x=line[i]
    z=len(x)
    a=x[:z-1]
    sentence.append(a)
sentence.append(line[i+1])
o=random.choice(sentence)
print(o)
path.close()