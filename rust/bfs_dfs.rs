fn bfs(node: &mut Vec<Vec<usize>>, visited: &mut Vec<usize>, start: usize)
{
    let mut q:VecDeque<usize> = VecDeque::new();

    visited[start] = 1;
    q.push_back(start);

    while !q.is_empty()
    {
        let pop = q.pop_front().unwrap();

        for i in &node[pop]
        {
            if visited[*i] == 0
            {
                visited[*i] = visited[pop] + 1;
                q.push_back(*i);
            }
        }
    }
}

fn dfs(node: &mut Vec<Vec<usize>>, visited: &mut Vec<usize>, cur: usize, cnt: usize)
{
    visited[cur] = cnt + 1;

    for next in 0..node[cur].len()
    {
        if visited[node[cur][next]] == 0
        {
            dfs(node, visited, node[cur][next], cnt + 1)
        }
    }
}
