def enqueue(queue, data):
    queue.append(data)

def dequeue(queue):
    if not queue:
        print("Queue is empty")
        return None
    return queue.pop(0)

queue = []
enqueue(queue, 10)
enqueue(queue, 20)
print(dequeue(queue))  