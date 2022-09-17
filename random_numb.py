from random import randint


def random_number(min_num: int, max_num: int, size: int):
    return [randint(min_num, max_num) for i in range(size)]
