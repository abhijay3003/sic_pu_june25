def create_circular_queue(size):
    return {
        'queue': [None] * size,
        'size': size,
        'front': -1,
        'rear': -1
    }

def enqueue(cq, value):
    next_pos = (cq['rear'] + 1) % cq['size']
    if next_pos == cq['front']:
        print("Queue is full")
        return
    if cq['front'] == -1:
        cq['front'] = 0
    cq['rear'] = next_pos
    cq['queue'][cq['rear']] = value

def dequeue(cq):
    if cq['front'] == -1:
        print("Queue is empty")
        return None
    value = cq['queue'][cq['front']]
    if cq['front'] == cq['rear']:
        cq['front'] = cq['rear'] = -1
    else:
        cq['front'] = (cq['front'] + 1) % cq['size']
    return value

def display_queue(cq):
    if cq['front'] == -1:
        print("Queue is empty")
        return
    i = cq['front']
    while True:
        print(cq['queue'][i], end=" ")
        if i == cq['rear']:
            break
        i = (i + 1) % cq['size']
    print()

cq = create_circular_queue(5)
enqueue(cq, 10)
enqueue(cq, 20)
enqueue(cq, 30)
display_queue(cq)     
dequeue(cq)
display_queue(cq)    