#볼록 껍질 알고리즘

def ccw(a, b, c): return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def convex_hull(coord):
    if len(coord) == 1: return coord
    
    up = []
    down = []
    
    for i in coord:
        while len(up) >= 2 and ccw(up[len(up) - 2], up[len(up) - 1], i) >= 0: up.pop()
        up.append(i)
        
    for i in reversed(coord):
        while len(down) >= 2 and ccw(down[len(down) - 2], down[len(down) - 1], i) >= 0: down.pop()
        down.append(i)
    
    up.reverse(); down.reverse()
    
    return down[:-1] + up[:-1]
