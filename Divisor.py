#Divisor generator
"""
test_number = input("Enter a number")

num = int(test_number)

def divisor(n):
    for i in range(n):
        x = len([i for i in range (1, n+1) if not n% i])
    return x

print (divisor(num))

"""

#Fibonnaci generator
a = int(input('Give amount: '))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(a)))

