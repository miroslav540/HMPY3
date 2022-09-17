import numbers
from tokenize import Number


import random_numb

numbers = random_numb.random_number(-10, 10, 5)
print(numbers)


def Sum_of_numbers(numbers2):

    sum: int = 0
    for i in numbers2:
        sum = sum + i
    return sum


numbers2 = numbers[1::2]
print(numbers2)

print(Sum_of_numbers(numbers2))
