def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

n = int(input("Enter number to compute factorial: "))
print(f"Factorial of {n} is: {factorial(n)}")