Number = int (input("Enter the number : "))
list = []
while(Number > 0):
    last_digit = Number % 10
    list.append(last_digit)
    Number= Number // 10
print("biggest digit in number is : ",max(list))



