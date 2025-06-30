size = int(input("Enter the size of the X shape (odd number recommended): "))
for i in range(size):
    for j in range(size):
        if j == i or j == size - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()