#! python3

from sys import exit

def sumOfSquares(low, high):
    return sum(i ** 2 for i in range(low, high))


def squareOfSum(low, high):
    return sum(range(low, high)) ** 2

print(squareOfSum(1, 101) - sumOfSquares(1, 101))
