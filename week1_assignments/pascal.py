Number_of_rows = int(input("Enter the number of rows for Pascal's Triangle: "))
for i in range(Number_of_rows):
    print(" " * (Number_of_rows - i), end="")  
    num = 1
    for j in range(i + 1):
        print(f"{num} ", end="")
        num = num * (i - j) // (j + 1)  
    print()