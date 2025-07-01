size = int(input("Enter the size of the square (odd number recommended): "))
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end="")  
        elif j == i or j == size - i - 1:
            print("*", end="")  
        else:
            print(" ", end="")  
    print()