def init(tree):
    N = len(tree) // 2
    
    for i in range(N - 1, 0, -1):
        tree[i] = max(tree[i * 2], tree[i * 2 + 1])
        
def update(tree, idx, val):
    idx += len(tree) // 2 - 1
    tree[idx] = val

    while idx > 1:
        idx //= 2
        tree[idx] = max(tree[idx * 2], tree[idx * 2 + 1])
        
def query(tree, idx1, idx2):
    res = 0

    idx1 += len(tree) // 2 - 1
    idx2 += len(tree) // 2 - 1

    while idx1 <= idx2:
        if idx1 % 2 == 1:
            res = max(res, tree[idx1])
            idx1 += 1

        if idx2 % 2 == 0:
            res = max(res, tree[idx2])
            idx2 -= 1

        idx1 //= 2
        idx2 //= 2

    return res
