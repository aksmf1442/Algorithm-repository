from collections import deque

m, n, k = map(int, input().split())
lis = [[0] * m for _ in range(n)]
result = 0
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
visited = [[0] * m for _ in range(n)]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if visited[nx][ny] == 1:
                continue
            
            if lis[nx][ny] == 1:    
                visited[nx][ny] = 1
                q.append((nx, ny))
            
    return 1
        

for _ in range(k):
    y, x = map(int, input().split())
    lis[x][y] = 1
    
for i in range(n):
    for j in range(m):
        if lis[i][j] == 1 and visited[i][j] == 0:
            result += bfs(i, j)

print(result)