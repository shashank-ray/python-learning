def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        factorial=1
        for i in range (n,1,-1):
            factorial *= i
        return factorial
result = factorial(5)
print(result)
    