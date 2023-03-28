def fib(n):
    return fib(n-1) + fib(n-2) if n > 1 else n

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(30))