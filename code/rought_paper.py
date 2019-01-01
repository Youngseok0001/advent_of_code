def mul(a, b):
    # a * b = a + a + a + .... a
    #       =  a + (b-1)*a
    #       =  a + a + (b-2)*a

    if b == 1:
        return a
    else:
        return mul(a, b - 1) + a


memo = {i: i for i in range(3)}


def fibo(n, memo):
    # f(n) = f(n-1) + f(n-2)
    # f(0) = 0
    # f(1) = 1

    if n in memo.keys():
        return memo[n]

    else:
        return fibo(n - 1, memo) + fibo(n - 2, memo)


def iterative_add(n):
    #n = n-1 + n
    if n == 1:
        return n
    else:
        return iterative_add(n - 1) + n


def factorial(n):
    # f(n) = f(n-1) * n
    # f(1) = 1

    if n == 1:
        return n
    else:
        return factorial(n - 1) * n


def count(n):
    # f(n) = 1 + f(n-1)
    # f(n) = 1
    if n == 1:
        return n

    else:
        return count(n - 1) + 1


def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])


def printMove(fr, to):
    print(" move from " + str(fr) + " to " + str(to))


def towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        towers(n - 1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n - 1, spare, to, fr)


def pascal(n):
    # [1]
    # [1][1]
    # [1][2][1]
    # [1][3][3][1]
    # [1][4][6][4][1]
    # pascal(n) = function(pascal(n-1)) + append(1)
    # pascal(1) = [1]
    # pascal(2) = [1]

    def pattern(input):
        output = []
        for idx in range(len(input) - 1):
            output.append(input[idx] + input[idx + 1])
        return output

    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    else:
        return [1] + pattern(pascal(n - 1)) + [1]



from random import random


def quick_sort(input):
    if len(input) <= 1:
        return input
    small, equal, large = [], [], []
    pivot = input[0]
    for i in input:
        if i < pivot:
            small.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            large.append(i)
    return quick_sort(small) + \
        sorted(equal) + \
        quick_sort(large)


print(mul(100, 3))
print(fibo(10, memo))
print(iterative_add(4))
print("factoral answer: " + str(factorial(10)))
print(count(10))
print(is_palindrome("ABCCBA"))
towers(2, "Source", "Target", "AUX")
print(pascal(6))
print(quick_sort([7, 100, 14, 1, 2, 3]))
print(fibo_pascal(7))
