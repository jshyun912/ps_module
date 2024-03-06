def cross(a, b): return a[0] * b[1] - a[1] * b[0]  # 외적
def vect(a, b): return (a[0] - b[0], a[1] - b[1]) # 벡터 계산 (b에서 a로 이동)

def line_intersection(p0, p1, q0, q1):
    q0_q1 = vect(q1, q0)
    p0_p1 = vect(p1, p0)
    p0_q0 = vect(q0, p0)
    
    par = cross(p0_p1, q0_q1) # 두 직선이 평행한가요?
    
    if par != 0: # 평행하지 않다면
        s = [cross(p0_q0, q0_q1), abs(par)]
        t = [cross(p0_q0, p0_p1), abs(par)]
        
        if par < 0: s[0], t[0] = -s[0], -t[0]
        
        if s[0] < 0 or s[0] > s[1] or t[0] < 0 or t[0] > t[1]: return 0 # 교점이 없다
        if s[0] == 0 or s[0] == s[1] or t[0] == 0 or t[0] == t[1]: return 1 # 교점이 한 선분의 끝
        else: return 2 # 교점이 하나
    
    p1_q0 = vect(q0, p1)
    p1_q1 = vect(q1, p1)

   # 선분이 한 직선위에 있는가?
    if cross(p0_p1, p1_q0) or cross(p0_p1, p1_q1) or cross(p0_q0, q0_q1) or cross(p1_q0, q0_q1): 
        return 0
    
    a, b = min(p0, p1), max(p0, p1)
    c, d = min(q0, q1), max(q0, q1)
    
    l, r = max(a, c), min(b, d)
    
    if l == r: return 1 # 교점이 한개
    if l < r: return 3 # 교점이 무한함
    return 0 # 없음

# 교점의 좌표를 반환하는 코드

from fractions import Fraction

def cross(a, b): return a[0] * b[1] - a[1] * b[0]
def vect(a, b): return (a[0] - b[0], a[1] - b[1])

def line_intersection_coord(p0, p1, q0, q1):
    q0_q1 = vect(q1, q0)
    p0_p1 = vect(p1, p0)
    p0_q0 = vect(q0, p0)
    
    par = cross(p0_p1, q0_q1)
    
    if par != 0:
        s = Fraction(cross(p0_q0, q0_q1), par)
        t = Fraction(cross(p0_q0, p0_p1), par)
        
        if 0 <= s <= 1 and 0 <= t <= 1:
            x = p0[0] + (p1[0] - p0[0]) * s
            y = p0[1] + (p1[1] - p0[1]) * s
            return (x, y)
        
        return
    
    p1_q0 = vect(q0, p1)
    p1_q1 = vect(q1, p1)

    if cross(p0_p1, p1_q0) or cross(p0_p1, p1_q1) or cross(p0_q0, q0_q1) or cross(p1_q0, q0_q1): 
        return
    
    a, b = min(p0, p1), max(p0, p1)
    c, d = min(q0, q1), max(q0, q1)
    
    l, r = max(a, c), min(b, d)
    
    if l == r: return l
    if l < r: return [l, r]
    return
