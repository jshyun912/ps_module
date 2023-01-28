#볼록 껍질 알고리즘

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

up = deque()
down = deque()

up.append(coord[0]); up.append(coord[1])
down.append(coord[0]); down.append(coord[1])

for i in range(2, N):
    while len(up) > 1:
        if ccw(up[-2], up[-1], coord[i]) <= 0:
            break
        up.pop()

    while len(down) > 1:
        if ccw(down[-2], down[-1], coord[i]) >= 0:
            break
        down.pop()

    up.append(coord[i])
    down.append(coord[i])
