fn gcd(mut a:usize, mut b:usize) -> usize
{
    let mut tmp;

    while b != 0
    {
        tmp = a;
        a = b;
        b = tmp % b;
    }

    a
}

fn lcm(a:usize, b:usize) -> usize { a * b / gcd(a, b) }
