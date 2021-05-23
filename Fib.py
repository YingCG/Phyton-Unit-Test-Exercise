
def i = 0

def fib_recursive(n):
    i += 1
    print(n)
    if (n <= 1):
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

print(fib_recursive(30))
print(i)