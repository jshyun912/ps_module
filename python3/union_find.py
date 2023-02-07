def find(x):
    global link
    if (x == link[x]):
        return x
    
    link[x] = find(link[x])

    return link[x]

def united(a, b):
    global link, size
    a = find(a)
    b = find(b)

    if a == b:
        return

    if size[a] < size[b]:
        temp = a
        a = b
        b = temp

    size[a] += size[b]
    link[b] = a
    
def reset():
  global link, size
  link = [ i for i in range(N) ]
  size = [ 1 for i in range(N) ]
