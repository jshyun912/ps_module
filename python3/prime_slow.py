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
