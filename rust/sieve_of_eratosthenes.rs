fn sieve_of_eratosthenes(n:usize) -> Vec<bool>
{
    let mut sieve:Vec<bool> = vec![true;n+1];

    let mut i = 2;

    while i * i <= n
    {
        if sieve[i]
        {
            let mut j = 2;

            while i * j <= n { sieve[i * j] = false; j += 1 }
        }

        i += 1
    }

    sieve
}
