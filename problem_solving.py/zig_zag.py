class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(n, edges):
    nodes = {}
    for u, v, side in edges:
        if u not in nodes:
            nodes[u] = Node(u)
        if v not in nodes:
            nodes[v] = Node(v)
        if side == 'L':
            nodes[u].left = nodes[v]
        else:
            nodes[u].right = nodes[v]
    return nodes[edges[0][0]]  

def zigzag_traversal(root):
    if not root:
        return []

    queue = [root]
    result = []
    left_to_right = True

    while queue:
        level_size = len(queue)
        level = []

        for i in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level = level[::-1]

        result += level
        left_to_right = not left_to_right

    return result

n = int(input())
edges = [input().split() for _ in range(n - 1)]
edges = [(int(u), int(v), d) for u, v, d in edges]

root = build_tree(n, edges)
output = zigzag_traversal(root)

for val in output:
    print(val, end=' ')