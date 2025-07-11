def are_mirror(n, tree1, tree2):
    pairs1 = set()
    pairs2 = set()

    for u, v, d in tree1:
        pairs1.add((u, v, d))

    for u, v, d in tree2:

        mirror_d = 'L' if d == 'R' else 'R'
        pairs2.add((u, v, mirror_d))

    return "yes" if pairs1 == pairs2 else "no"


n = int(input())           
tree1 = [input().split() for _ in range(n - 1)]
tree2 = [input().split() for _ in range(n - 1)]

tree1 = [(int(u), int(v), d) for u, v, d in tree1]
tree2 = [(int(u), int(v), d) for u, v, d in tree2]

print(are_mirror(n, tree1, tree2))