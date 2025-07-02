import time
def liner_search( search_element , arr):
    if(arr[0]== search_element):
        print("element found!")
    
    else :
        liner_search( search_element ,arr[1:])

search_element = 10 
arr = [1,2,3,4,5,6,7,8,9,10]
start = time.time()
liner_search(search_element,arr)
end = time.time()
print("time taken to complete :" ,start-end)