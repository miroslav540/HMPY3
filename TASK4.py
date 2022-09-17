'''без рекурсии'''
# def Binary(num):
#     bin = []
#     while num > 0:
#         bin.append(num % 2)
#         num //= 2
#     return bin


# bin = Binary(int(input('-> ')))
# print(bin[::-1])


'''рекурсия'''
bin = []
def Binary(num, n):
    if num == 0:
        return 1
    else:
        bin.insert(n, num % 2)
        return Binary(num//2, n - 1)


num = Binary(int(input('-> ')), - 1)
print(bin)
