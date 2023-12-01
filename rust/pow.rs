fn pow(mut a:usize, mut b:usize, c: usize) -> usize
{
    let mut res = 1;

    while b > 0
    {
        if b % 2 != 0
        {
            res *= a;
            res %= c;
        }

        a *= a;
        a %= c;
        b /= 2;
    }

    res
}
