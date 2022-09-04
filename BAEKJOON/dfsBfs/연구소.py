#다시 풀어보기

n, m = map(int, input().split())
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
board = []
temp = [[0] * m for _ in range(n)]
result = 0
for i in range(n):
    board.append(list(map(int, input().split())))


def virus(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx, ny)
    pass


def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        s = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    s += 1
        result = max(result, s)
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                count += 1
                dfs(count)
                board[i][j] = 0
                count -= 1

dfs(0)
print(result)