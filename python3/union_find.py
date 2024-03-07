# 분리 집합 알고리즘

def find(x, link):
    if (x == link[x]): return x
    
    link[x] = find(link[x], link)

    return link[x]

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
