

def distance_from_zero(number):
    if type(number)== int:
        return (number)
    elif type (number)== float:
        return (number)
    else:
        return"nope"

print(distance_from_zero(-5.5))
print(distance_from_zero(5))
print(distance_from_zero("what"))


def see_year(year):



    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));



year = 2000
if (see_year(year)):
    print("true")
else:
    print("false")

ages = [20, 30, 40, 50, 60]

ages = list(map(lambda x: x + 1, ages))

print(ages)





grades =[20 , 10, 90, 85, 40, 75, 65, 64, 12, 74, 71, 98, 50]





















dog_ages = [12, 8, 4, 2, 6,4,4,5 ]

dog_ages = list(map(lambda x: x *7, dog_ages))

print(dog_ages)





transactions = [51.0, 49.99, 80.99, 67.99, 20.52, 23.49]

transactions = 51.0 + 49.99 + 80.99 + 67.99 + 20.52 + 23.49

print(transactions)

















