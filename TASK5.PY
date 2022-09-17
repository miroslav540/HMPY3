def Fibonacci_pos(num):
    Fibonacci_positive = []
    fib1 = 0
    fib2 = 1
    for i in range(num + 1):
        if i == 0:
            Fibonacci_positive.insert(i, fib1)
        elif i == 1:
            Fibonacci_positive.insert(i, fib2)
        else:
            Fibonacci_positive.insert(i, fib1+fib2)
            time = fib2
            fib2 = fib1 + fib2
            fib1 = time
    return Fibonacci_positive


Fibonacci_positive = Fibonacci_pos(int(input('-> ')))
print(Fibonacci_positive)


def Fibonacci_Neg(num):
    Fibonacci_Negative = []
    fib1 = 1
    fib2 = -1
    for i in range(num):
        if i == 0:
            Fibonacci_Negative.insert(i, fib1)
        elif i == 1:
            Fibonacci_Negative.insert(i, fib2)
        else:
            Fibonacci_Negative.insert(i, fib1 - fib2)
            time = fib2
            fib2 = fib1 - fib2
            fib1 = time
    return Fibonacci_Negative


Fibonacci_Negative = Fibonacci_Neg(int(input('-> ')))
print(Fibonacci_Negative)

All_Fib = str(Fibonacci_Negative[::-1] + Fibonacci_positive)
print(All_Fib)
