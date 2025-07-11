class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    return node.height if node else 0

def update_height(node):
    if node:
        node.height = 1 + max(height(node.left), height(node.right))

def get_balance(node):
    return height(node.left) - height(node.right) if node else 0

def rotate_left(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    update_height(z)
    update_height(y)
    print(f"RR Rotation at node {z.val}")
    return y

def rotate_right(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    update_height(z)
    update_height(y)
    print(f"LL Rotation at node {z.val}")
    return y

def insert(node, key, show_rotation=False):
    if not node:
        return Node(key)
    if key < node.val:
        node.left = insert(node.left, key, show_rotation)
    else:
        node.right = insert(node.right, key, show_rotation)

    update_height(node)
    bf = get_balance(node)

    if bf > 1 and key < node.left.val:
        if show_rotation: print(f"LL Rotation at node {node.val}")
        return rotate_right(node)
    if bf < -1 and key > node.right.val:
        if show_rotation: print(f"RR Rotation at node {node.val}")
        return rotate_left(node)
    if bf > 1 and key > node.left.val:
        node.left = rotate_left(node.left)
        if show_rotation: print(f"LR Rotation at node {node.val}")
        return rotate_right(node)
    if bf < -1 and key < node.right.val:
        node.right = rotate_right(node.right)
        if show_rotation: print(f"RL Rotation at node {node.val}")
        return rotate_left(node)

    return node

def get_min(node):
    while node.left:
        node = node.left
    return node

def delete(node, key):
    if not node:
        return node
    if key < node.val:
        node.left = delete(node.left, key)
    elif key > node.val:
        node.right = delete(node.right, key)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        temp = get_min(node.right)
        node.val = temp.val
        node.right = delete(node.right, temp.val)

    update_height(node)
    bf = get_balance(node)

    if bf > 1 and get_balance(node.left) >= 0:
        return rotate_right(node)
    if bf > 1 and get_balance(node.left) < 0:
        node.left = rotate_left(node.left)
        return rotate_right(node)
    if bf < -1 and get_balance(node.right) <= 0:
        return rotate_left(node)
    if bf < -1 and get_balance(node.right) > 0:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def preorder(node):
    if node:
        print(node.val, end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)

print("Choose operation:")
print("1 → Insert into AVL Tree")
print("2 → Delete from AVL Tree")
print("3 → Demo All Rotations")
choice = int(input())

root = None

if choice == 1:
    n = int(input("Enter number of nodes to insert: "))
    values = list(map(int, input("Enter space-separated values to insert: ").split()))
    for v in values:
        root = insert(root, v)
    print("Preorder traversal after insertion:")
    preorder(root)

elif choice == 2:
    n = int(input("Enter number of nodes to insert: "))
    values = list(map(int, input("Enter space-separated values to insert: ").split()))
    k = int(input("Enter the key to delete: "))
    for v in values:
        root = insert(root, v)
    root = delete(root, k)
    print("Inorder traversal after deletion:")
    inorder(root)

elif choice == 3:
    n = int(input("Enter number of elements for rotation demo: "))
    values = list(map(int, input("Enter space-separated values for rotation test: ").split()))
    for v in values:
        root = insert(root, v, show_rotation=True)
    print("Preorder traversal after rotations:")
    preorder(root)