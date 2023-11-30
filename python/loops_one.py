def fib(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(3, n+1):
            a, b = b, a + b
        return b


n = 7  
result = fib(n)
print(f"The {n}-th Fibonacci number is: {result}")