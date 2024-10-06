def dedup(a):
    if len(a) == 0: return []
    
    res = [ a[0] ]
    
    tmp = a[0]
    for i in a[1:]:
        if i != tmp:
            tmp = i
            res.append(tmp)
            
    return res
