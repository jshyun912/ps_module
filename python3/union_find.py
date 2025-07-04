# 분리 집합 알고리즘

def find(x, link):
    to_change = []

    x = link[x]
    while x != link[x]:
        to_change.append(x)
        x = link[x]

    while to_change: link[to_change.pop()] = x

    return x

def united(a, b, link, size):
    a = find(a, link)
    b = find(b, link)

    if a == b: return

    if size[a] < size[b]: a, b = b, a

    size[a] += size[b]
    size[b] = 0
    link[b] = a
    
def reset():
  global link, size
  link = [ i for i in range(N) ]
  size = [ 1 for i in range(N) ]
