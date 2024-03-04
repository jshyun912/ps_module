def cross(a, b): return a[0] * b[1] - a[1] * b[0]
def vect(a, b): return (a[0] - b[0], a[1] - b[1])
def dist_euclid(a, b): return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])

def rotating_calipers(ch): # CONVEX HULL FIRST
    ch_len = len(ch)
    if ch_len == 1: return (ch[0], ch[0])
    
    C, D = 1, 2 % ch_len
    max_dist = 0
    res = (0, 0)
    
    for A in range(ch_len):
        B = (A + 1) % ch_len
        
        while 1:
            dist = dist_euclid(ch[A], ch[C])
        
            if dist > max_dist:
                res = (ch[A], ch[C])
                max_dist = dist
            
            if cross(vect(ch[B], ch[A]), vect(ch[D], ch[C])) <= 0:
                break
            
            C = (C + 1) % ch_len
            D = (C + 1) % ch_len
    
    return res
