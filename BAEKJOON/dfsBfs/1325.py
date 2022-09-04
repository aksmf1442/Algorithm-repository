import sys
from collections import deque

def bfs(node):
    visited = [False] * (n + 1)
    visited[node] = True
    queue = deque([node])
    count = 0
    while True:
        node = queue.popleft()
        count += 1
        for nd in graph[node]:
            if visited[nd]:
                continue

            queue.append(nd)
            visited[nd] = True

        if len(queue) == 0:
            break
    return count

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


result = [0] * (n+1)
for i in range(1, n + 1):
    result[i] = bfs(i)

maxValue = max(result)
for i in range(1, n+1):
    if result[i] == maxValue:
        print(i, end=" ")

"""효율적인 해킹
    1. graph에 신뢰관계인 컴퓨터를 연결해준다.
    2. result에 bfs를 통해 얻은 해킹한 컴퓨터 수를 초기화해둔다.
    3. maxValue인 값을 각 컴퓨터의 result의 값과 비교해서 같으면 출력하도록 한다.
"""