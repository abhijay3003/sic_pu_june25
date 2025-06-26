Number = int(input("Enter the number: "))
Digits = []
while Number > 0:
    Digits.append(Number % 10)
    Number //= 10

even_position_sum = 0
for i in range(len(Digits)):
    if (i + 1) % 2 == 0:  
        even_position_sum += Digits[i]

print("Sum of digits at even positions:", even_position_sum)