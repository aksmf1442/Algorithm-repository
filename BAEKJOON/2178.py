from collections import deque

def bfs(data, n, m, visited):
    q = deque([(0,0,0)])
    dx, dy = [0,0,-1,1],[1,-1,0,0]
    answer = float('inf')
    while q:
        x, y, value = q.popleft()
        if data[x][y] == '0' or visited[x][y] == 1:
            continue
        if x == n and y == m:
            answer = min(answer, value+1)
            continue
        visited[x][y] = 1
        value +=1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx > n or ny < 0 or ny > m:
                continue
            if data[nx][ny] == '0' or visited[nx][ny] == 1:
                continue
            q.append((nx,ny,value))
    return answer


n, m = map(int, input().split())
data = []
for _ in range(n):
    a = input()
    data.append(a)
visited = [[0]*m for _ in range(n)]
if data[0][0] == '1':
    result = bfs(data, n-1, m-1, visited)
    print(result)
else:
    print(0)