n, x, y = map(int, input("Enter the numbers n, x, y separated by spaces: ").split())
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

numbers.sort()

if 0 < y < n:
    p = numbers[y] - numbers[y - 1] - 1
    print("Result:", p)
else:
    print("Invalid value for y. It must be between 1 and", n - 1)