from collections import deque

n, m, k, x = map(int, input().split())
direction = [[] for _ in range(n+1)]

for _ in range(m):
    nx, ny = map(int, input().split())
    direction[nx].append(ny)

visited = [-1] * (n + 1)
visited[x] = 0
candidate = deque([(x, 0)])

while candidate:
    x, y = candidate.popleft()
    for i in direction[x]:
        if visited[i] != -1:
            continue
        candidate.append((i, y + 1))
        visited[i] = y + 1

check = False
for i in range(len(visited)):
    if visited[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
