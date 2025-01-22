from collection import deque

idx = ((1, 0), (-1, 0), (0, -1), (0, 1))

def compare(): return 0

def grid_bfs(visited, start, check = 1, comp = ()):
    visited[start[0]][start[1]] = check

    q = deque([start])
    
    while q:
        a, b = q.popleft()
        
        for i, j in idx:
            r, c = a + i, b + j
            
            if not (0 <= r < len(visited) and 0 <= c < len(visited[0])): continue
            if compare(): continue
            if visited[r][c]: continue
            
            visited[r][c] = check
            
            q.append((r, c))

def grid_dfs(visited, start, check = 1, comp = ()):
    a, b= start
    
    visited[start[0]][start[1]] = check
    
    for i, j in idx:
        r, c = a + i, b + j
            
        if not (0 <= r < len(visited) and 0 <= c < len(visited[0])): continue
        if compare(): continue
        if visited[r][c]: continue
            
        grid_dfs(visited, (r, c), check, comp)
