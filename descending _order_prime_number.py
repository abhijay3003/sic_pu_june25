Number1 = int(input("Enter the Number : "))
Number2 = int(input("Enter the another Number"))
largest_number = 0
smallest_number = 0
if(Number1 < Number2):
    largest_number = Number2
    smallest_number = Number1
else :
    largest_number= Number1
    smallest_number = Number2
print("Prime Number are : " , end=' ')
for i in range(largest_number,smallest_number,-1):
    No_of_factors = 0
    for j in range(1,i+1):
        if(i % j == 0):
            No_of_factors += 1
    if(No_of_factors == 2):
        print(i,end=' ')