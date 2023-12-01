const INF:i64 = 0x3f3f3f3f3f3f3f3f;

fn bellman_ford(node:&Vec<(usize, usize, i64)>, n:usize, start:usize) -> Vec<i64>
{
    let mut dist:Vec<i64> = vec![INF;n + 1];

    dist[start] = 0;

    for _ in 0..n - 1
    {
        for i in node
        {
            if dist[i.0] == INF { continue }

            dist[i.1] = i64::min(dist[i.1], dist[i.0] + i.2) 
        }
    }

    for _ in 0..n - 1
    {
        for i in node
        {
            if dist[i.0] == INF { continue }

            if dist[i.1] > dist[i.0] + i.2 { println!("음수 사이클") }
        }
    }    

    dist
}
