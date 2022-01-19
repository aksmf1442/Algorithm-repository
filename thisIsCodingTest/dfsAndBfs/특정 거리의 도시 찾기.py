from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] > 0:
                continue
            visited[i] = visited[node] + 1
            queue.append(i)
            
    

n, m, k, s = map(int, input().split())
visited = [0 for i in range(n+1)]
graph = [[] for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)

bfs(s)

result = []
for i in range(len(visited)):
    if visited[i] == k:
        result.append(i)

if not result:
    print(-1)
else:
    for i in result:
        print(i)
