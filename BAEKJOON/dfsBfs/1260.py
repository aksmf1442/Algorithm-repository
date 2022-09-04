from collections import deque

def dfs(node):
    visited.append(node)
    result.append(node)

    for i in sorted(graph[node]):
        if i in visited:
            continue
        dfs(i)

def bfs(node):
    visited.append(node)
    result.append(node)
    queue = deque([node])
    while True:
        node = queue.popleft()

        for i in sorted(graph[node]):
            if i in visited:
                continue
            queue.append(i)
            result.append(i)
            visited.append(i)

        if not queue:
            break

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = []
visited = []
dfs(v)
for i in result:
    print(i, end=" ")
print()

result = []
visited = []
bfs(v)
for i in result:
    print(i, end=" ")

"""
    파이썬 풀이(dfs 통한 풀이)
    1. graph에 간선을 초기화하고 result, visited를 초기화한다.
    2. dfs통해 순서대로 result에 담고 그대로 출력하는데, 이 때 간선을 오름차순으로 정렬해주어야한다.
    
    파이썬 풀이(bfs 통한 풀이)
    1. graph에 간선을 초기화하고 result, visited를 초기화한다.
    2. bfs통해 순서대로 result에 담고 그대로 출력하는데, 이 때 간선을 오름차순으로 정렬해주어야한다.
    
"""