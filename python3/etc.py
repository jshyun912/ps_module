def dedup(a):
    if len(a) == 0: return []
    
    res = [ a[0] ]
    
    tmp = a[0]
    for i in a[1:]:
        if i != tmp:
            tmp = i
            res.append(tmp)
            
    return res
# 정렬된 배열에서 중복제거

def init_prefix_sum_2d(x):
    r, c = len(x), len(x[0])
    
    for i in range(1, r):
        for j in range(1, c):
            x[i][j] = x[i][j-1] + x[i-1][j] - x[i-1][j-1] + x[i][j]
            
def query_prefix_sum_2d(x, c, d, a, b):
    return x[a][b] - x[a][d-1] - x[c-1][b] + x[c-1][d-1]

# 2차원 누적합, cd가 ab보다 작아야함, cd를 포함하는 범위의 합을 구한다
