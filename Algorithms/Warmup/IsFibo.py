import math


def is_square(n):
    return math.sqrt(n).is_integer()


def isFibo(n):
    if is_square(5 * n**2 + 4) or is_square(5 * n**2 - 4):
        print "IsFibo"
    else:
        print "IsNotFibo"

n = input()

for i in range(n):
    num = input()
    isFibo(num)
