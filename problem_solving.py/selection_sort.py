list = list(map(int, input("Enter the elements of the list separated by space: ").split()))
N = len(list)

for i in range(1, N):  
    element = list[i-1]
    position = i-1
    
    for j in range(i-1, N):  # j = i-1 to N-1
        if list[j] < element:
            element = list[j]
            position = j
    list[i-1] , list[position] = list[position] , list[i-1]

print("Sorted list:", list)