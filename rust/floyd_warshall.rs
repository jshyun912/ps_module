fn floyd_warshall(dist:&mut Vec<Vec<i64>>, n:usize)
{
    for i in 1..=n 
    { 
        for j in 1..=n 
        { 
            for k in 1..=n 
            { 
                dist[j][k] = i64::min(dist[j][k], dist[j][i] + dist[i][k])
            } 
        } 
    }
}
