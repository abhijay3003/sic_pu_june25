my_list = list(map(int, input("Enter the elements of the list separated by space: ").split()))
n = len(my_list)
for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            swapped = True
    
    if not swapped:
        break

print("Sorted list:", my_list)