#! python3

from sys import exit

def isPalindrome(input):
    inputStr = str(input)

    for i in range(len(inputStr)):
        if inputStr[i] != inputStr[-(i + 1)]:
            return False

    return True

def findFactor(input, high, low):
    for i in range(high, low, -1):
        if input % i == 0:
            return i
    
    return 1

for i in range(997799, 10000, -1):
    if isPalindrome(i):
        factor = findFactor(i, 999, 100)

        if i / factor < 999:
            print('palindrome: ' + str(i))
            print('number 1: ' + str(factor))
            print('number 2: ' + str(i / factor))
            exit()

