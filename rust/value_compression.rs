fn compression(ary: &Vec<i64>) -> Vec<i64>
{
    let mut res:Vec<i64> = vec![];

    for i in ary { res.push(*i) }

    res.sort(); res.dedup();

    res
}

fn binary_search(ary: &[i64], to_find: i64) -> (usize, usize)
{
    let (mut lower_bound, mut upper_bound) = (0, ary.len());

    while lower_bound + 1 < upper_bound
    {
        let mid = (lower_bound + upper_bound) / 2;

        if ary[mid] <= to_find { lower_bound = mid }
        else { upper_bound = mid }
    }

    (lower_bound, upper_bound)
}
