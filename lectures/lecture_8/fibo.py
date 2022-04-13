import os
import sys


a = 2


class Hello:
    """I am class which greets"""
    pass

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(dir())
if __name__ == "__main__":
    fib2(int(sys.argv[1]))