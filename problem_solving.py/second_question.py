num_of_req = int(input('Enetr the number of requests : '))
requests = list(map(int, input("enter the each requests allocation / deallocations : ").split()))
total = 0
for i in range(0, num_of_req, 2):
    total += requests[i]
print("Total number of units of memory allocated / deallocation by the server 1 after processing all the requests : ",total)

