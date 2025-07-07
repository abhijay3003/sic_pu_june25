def push(stack, data):
    stack.append(data)

def pop(stack):
    if not stack:
        print("Stack is empty")
        return None
    return stack.pop()


stack = []
push(stack, 100)
push(stack, 200)
print(pop(stack)) 