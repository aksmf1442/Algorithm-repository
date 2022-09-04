def dfs(node):
    visited[node] = 1
    for currentNode in graph[node]:
        if visited[currentNode]:
            continue
        dfs(currentNode)


n, m = map(int, input().split())
visited = [0] * (n + 1)
result = 0
graph = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1):
    if visited[i]:
        continue
    dfs(i)
    result += 1
print(result)
