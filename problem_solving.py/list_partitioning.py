n, x, y = map(int, input("Enter the numbers n, x, y separated by spaces: ").split())
numbers = list(map(int, input(f"Enter {n} numbers separated by spaces: ").split()))
numbers.sort()

if 0 < y < n:
    p = numbers[y] - numbers[y - 1] - 1
    print(p)
else:
    print("Invalid value for y. It must be between 1 and", n - 1)