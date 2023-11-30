use std::collections::*;
use std::cmp::*;

fn dijkstra(node: &mut [Vec<(usize, usize)>], dist: &mut [usize], start: usize)
{
    let mut pq:BinaryHeap<Reverse<(usize, usize)>> = BinaryHeap::new();
    dist[start] = 0;
    pq.push(Reverse((0, start)));

    while !pq.is_empty()
    {
        let pop = pq.pop().unwrap().0;

        if dist[pop.1] != pop.0 { continue }

        for i in &node[pop.1]
        {
            if dist[i.1] > pop.0 + i.0
            {
                dist[i.1] = pop.0 + i.0;
                pq.push(Reverse((dist[i.1], i.1)))
            }
        }
    }
} 

// 데이크스트라 알고리즘
// 튜플 구조 : (거리, 노드)
