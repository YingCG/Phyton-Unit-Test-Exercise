#Divisor generator
def divisor(n):
    for i in range(n):
        x = len([i for i in range (1, n+1) if not n% i])
    return x

#Fibonnaci generator
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
