Number_1, Number_2, Number_3 = map(int, input('Enter 3 numbers separated by space: ').split())
if(Number_1<=Number_2 and Number_3<=Number_2):
    print(Number_2,"is the smallest")
elif(Number_2<=Number_3 and Number_1 <= Number_3):
    print(Number_3,"is the smallest")
else:
    print(Number_2,"is the smallest")