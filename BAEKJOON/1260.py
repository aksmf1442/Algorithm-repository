## DFS와 BFS

from collections import deque
n, m, v = map(int, input().split())
data = [[] for _ in range(n+1)]

# 양방향으로 간선 추가
for _ in range(m):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

def dfs(start):
    print(start, end=' ')
    for node in sorted(data[start]):
        if node not in visited:
            visited.append(node)
            dfs(node)

def bfs(start):
    visited = []
    q = deque([start])
    visited.append(start)

    while q:
        node = q.popleft()
        print(node, end=' ')
        for n in sorted(data[node]):
            if n not in visited:
                visited.append(n)
                q.append(n)

visited = [v]
dfs(v)
print()
bfs(v)