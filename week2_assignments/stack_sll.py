def push(stack, data):
    stack.insert(0, data)

def pop(stack):
    if not stack:
        print("Stack is empty")
        return None
    return stack.pop(0)


stack = []
push(stack, 5)
push(stack, 15)
print(pop(stack))  