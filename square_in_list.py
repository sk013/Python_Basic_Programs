from typing import List


def square(l):
    tmp = []
    for i in l:
        tmp.append(i**2)
    return tmp

numbers = list(range(1,11))
print(square(numbers))