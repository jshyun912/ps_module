fn matrix_pow(a: &Vec<Vec<usize>>, mut b: usize, md: usize) -> Vec<Vec<usize>>
{
    let mut res = vec![];
    let n = a.len();

    for i in 0..n
    {
        let mut tmp = vec![];

        for j in 0..n
        {
            if i == j { tmp.push(1) }
            else { tmp.push(0) }
        }

        res.push(tmp)
    }

    let mut mat = a.clone();

    while b > 0
    {
        if b & 1 == 1 { res = matrix_multi(&mat, &res, md) }
        mat = matrix_multi(&mat, &mat, md);
        b >>= 1;
    }

    res
}

fn matrix_multi(a: &Vec<Vec<usize>>, b: &Vec<Vec<usize>>, md: usize) -> Vec<Vec<usize>>
{
    let mut res = vec![];
    let (a_r, rc, b_c) = (a.len(), a[0].len(), b[0].len());

    for _ in 0..a_r { res.push(vec![0;b_c]) }

    for i in 0..a_r
    {
        for j in 0..b_c
        {
            for k in 0..rc
            {
                res[i][j] = (res[i][j] + (a[i][k] * b[k][j]) % md) % md;
            }
        }
    }

    res
}
