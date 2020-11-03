from functools import reduce
# exercise 1
grades = [20, 10, 90, 85, 40, 75, 65, 64, 12, 74, 71, 98, 50]
def my_func(x):
   if x >= 70:
     return True
   else:
     return False
grades = list(filter(my_func, grades))
print(grades)



# exercise 2
dog_ages = [12, 8, 4, 2, 6,4,4,5 ]
dog_ages = list(map(lambda x: x *7, dog_ages))
print(dog_ages)


# exercise 3
from  functools import reduce
transactions = [51.0, 49.99, 80.99, 67.99, 20.52, 23.49]

for i in transactions:
    print(i, end="")