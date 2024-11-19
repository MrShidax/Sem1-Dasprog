def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_sequence(N):
    fib = []
    for i in range(N):
        fib.append(fibonacci(i))
    return fib

N = int(input())
fib_sequence = fibonacci_sequence(N)
print(f"The first {N} terms of the Fibonacci sequence are: {fib_sequence}")