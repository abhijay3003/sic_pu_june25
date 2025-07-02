def binary_search(search_element, arr):
    mid = len(arr) // 2
    if arr[mid] == search_element:
        return True
    elif arr[mid] > search_element:
        return binary_search(search_element, arr[:mid])
    else:
        return binary_search(search_element, arr[mid+1:])

search_element = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
found = binary_search(search_element, arr)

if found:
    print("element found")
else:
    print("element not found")