def dfs(count, node):
    global result
    if node == y:
        result = count
        return

    for currentNode in graph[node]:
        if visited[currentNode]:
            continue
        visited[currentNode] = 1
        dfs(count + 1, currentNode)
        visited[currentNode] = 0

n = int(input())
graph = [[] for _ in range(n+1)]
x, y = map(int, input().split())
result = -1
for _ in range(int(input())):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [0] * (n + 1);
dfs(0, x)
print(result)

