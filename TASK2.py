import random_numb
First_List = random_numb.random_number(1, 10, 6)
print('First list', First_List)


def Multiplication_Alem(First_List):
    if len(First_List) % 2 == 0:
        size = len(First_List)/2
    else:
        size = int((len(First_List)/2)+0, 5)

    Res_List = []
    i = 0
    while i <= size - 1:
        Res_List.append(First_List[i]*First_List[(i+1)*-1])
        i += 1
    return Res_List


print('Res_List    ', Multiplication_Alem(First_List))
