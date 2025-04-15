def sieve_of_eratosthenes(n):
    sieve = [ 0 for _ in range(n + 1) ]
    
    sieve[0] = 1
    sieve[1] = 1
    
    a = 2
    
    while 2 * a <= n:
        sieve[2 * a] = 1
        a += 1
        
    a = 3
    
    while a * a <= n:
        if sieve[a]:
            a += 2
            continue
        
        b = 2
        while a * b <= n:
            sieve[a * b] = 1
            b += 1
            
        a += 2
        
    return sieve

def list_prime(sieve):
    res = []
    for i, j in enumerate(sieve):
        if j == 0:
            res.append(i)

    return res

def is_prime(n):
    if n <= 1:
        return False
    
    a = 2;

    while a * a <= n:
        if n % a == 0:
            return False
        a += 1
        
    return True

def is_prime(N):
    if N > 2 and N & 1 == 0: return 0
    if N == 1 or N == 0: return 0

    test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for i in test:
        if i == N: return 1

        d = N - 1
        flt = pow(i, d, N)

        while ~d & 1:
            if flt == N - 1: break
            d >>= 1
            flt = pow(i, d, N)

        if d & 1 and flt != 1 and flt != N - 1:
            return 0

    return 1
