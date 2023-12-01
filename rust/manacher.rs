fn manacher(s:&String) -> Vec<usize>
{
    let mut s2:Vec<char> = vec!['.']; 

    for i in s.chars() { s2.push(i); s2.push('.') }
    let len = s2.len();

    let mut dp:Vec<usize> = vec![0;len];

    let mut max_pal = 0;

    for i in 0..len
    {
        if i <= dp[max_pal] + max_pal
        {
            let l = max_pal * 2 - i;
            dp[i] = usize::min(dp[l], dp[max_pal] + max_pal - i)
        }

        while i >= dp[i] + 1 && i + dp[i] + 1 < len && s2[i - dp[i] - 1] == s2[i + dp[i] + 1] { dp[i] += 1 }

        if dp[max_pal] + max_pal < dp[i] + i { max_pal = i }
    }

    dp
}
