fn init()
{
    let mut tree:Vec<usize> = vec![0;1 << 21];
    for i in 0..n { tree[i + (1 << 20)] = scanner.next().unwrap().unwrap() }
    for i in (1..=(1 << 20) - 1).rev() { tree[i] = tree[i * 2] + tree[i * 2 + 1] }
}

fn update(tree:&mut Vec<usize>, mut a:usize, b:usize)
{
    a += (1 << 20) - 1;

    tree[a] = b;

    a >>= 1;

    while a > 0 { tree[a] = tree[a * 2] + tree[a * 2 + 1]; a >>= 1 }
}

fn query (tree:&Vec<usize>, mut a:usize, mut b:usize) -> usize
{
    let mut res = 0;

    a += (1 << 20) - 1; b += (1 << 20) - 1;

    while a <= b
    {
        if a & 1 == 1 { res += tree[a]; a += 1 }
        if b & 1 == 0 { res += tree[b]; b -= 1 }

        a >>= 1; b >>= 1;
    }

    res
}
