nth_term = int(input("Enter the term : "))
digit1 = 1
digit2 = 2
fibo_list =[digit1,digit2]
for i in range(2,nth_term):
    third_digit = digit1 + digit2
    digit1 = digit2
    digit2 = third_digit
    fibo_list.append(third_digit)
print("{}th fibo number is : {}".format(nth_term,fibo_list[nth_term - 1]))