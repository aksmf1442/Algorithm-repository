from collections import deque

def bfs(x, y, resultX, resultY):
    q = deque()
    q.append([x, y])
    a[x][y] = 1
    while q:
        x, y = q.popleft()

        if x == resultX and y == resultY:
            return a[x][y] - 1

        for i in range(8):
            nx, ny = dx[i] + x, dy[i] + y
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if a[nx][ny] != 0:
                continue
            q.append([nx, ny])
            a[nx][ny] = a[x][y] + 1

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

for _ in range(int(input())):
    l = int(input())
    a = [[0] * l for _ in range(l)]
    x, y = map(int, input().split())
    resultX, resultY = map(int, input().split())
    print(bfs(x, y, resultX, resultY))
