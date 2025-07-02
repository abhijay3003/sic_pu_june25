import time
def liner_search( search_element , arr):
    if(arr[0]== search_element):
        return "element found"
    
    else :
         return liner_search( search_element ,arr[1:])

search_element = 10 
arr = [1,2,3,4,5,6,7,8,9,10]
start = time.time()
k=liner_search(search_element,arr)
print(k)
end = time.time()
print("time taken to complete :" ,end-start)