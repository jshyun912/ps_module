fn find(a:usize, link:&mut Vec<usize>) -> usize
{
    if a == link[a] { return a }
    link[a] = find(link[a], link);
    link[a]
}

fn unite(a:usize, b:usize, link:&mut Vec<usize>, size:&mut [usize], kid:&mut [usize])
{
    let mut x = find(b, link);
    let mut y = find(a, link);

    if x == y { return }

    if size[x] < size[y] { swap(&mut x, &mut y) }

    size[x] += size[y];
    size[y] = 0;
    kid[x] += kid[y];
    kid[y] = 0;
    link[y] = x
}
