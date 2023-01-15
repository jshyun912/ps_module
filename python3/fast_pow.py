def POW(a, b):
    res = 1

    while b > 0:
        if b % 2 != 0:
            res *= a
        a *= a
        b //= 2

    return res
  
  def POW(a, b, c):
    res = 1

    while b > 0:
        if b % 2 != 0:
            res *= a
            res %= c
        a *= a
        a %= c
        b //= 2

    return res
