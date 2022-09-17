Spisok_numbers = [4.07, 5.1, 8.2444, 6.98] #1.1, 1.2, 3.1, 5.17, 10.02
print('Spisok of numbers -> ', Spisok_numbers)
Integer_numbers = []
for i in Spisok_numbers:
    Integer_numbers.append(str(str(i).split('.')[1]))
print('Second variant ', Integer_numbers)


def Min_Max(Integer_numbers):
    different = 0
    maximum = max(Integer_numbers)
    minimum = min(Integer_numbers)
    print('min -> ', minimum, 'max -> ', maximum)
    if int(maximum) < 10:
        maximum = int(maximum) * 10
        different = int(maximum) - int(minimum)
    print(different)
    return different


Min_Max(Integer_numbers)
