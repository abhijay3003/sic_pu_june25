import time
search_element= 10

arr = [1,2,3,4,5,6,7,8,9,10]
found  = False
i = 0
start = time.time()
while not found :
    
    if (arr[i]== search_element):
        found = True
    else :
        i= i+1
end = time.time()
if(found ):
    print("element found")
else :
      print("element not found")
print("time taken to complete :" ,end-start)

       