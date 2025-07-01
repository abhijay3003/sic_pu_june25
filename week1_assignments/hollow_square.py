Length_of_square = int(input("Enter the length of Square : "))
for i in range(1,Length_of_square+1):
    if (i == 1):
        print("* " * Length_of_square)
    elif (i>=2 and i<Length_of_square):
           print("*"," " * Length_of_square,"*")
    else :
          print("* " * Length_of_square)