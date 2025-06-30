Number_of_lines = int(input("Enter the number of lines: "))
for i in range(1, Number_of_lines + 1):
    print(" " * (Number_of_lines - i), "*" * (2 * i - 1))