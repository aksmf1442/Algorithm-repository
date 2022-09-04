n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = 0


def clean():
    board[r][c] = 2


dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

count = 0
isBreak = False
while not isBreak:
    if board[r][c] == 0:
        clean()
        count = 0
        result += 1
    # 현재 바라보는 방향의 왼쪽으로 돌기
    d = (d - 1) % 4
    nx, ny = r + dx[d], c + dy[d]

    if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] != 0:
        count += 1
    else:
        r, c = nx, ny

    # 모든 방향 확인 후 후진하기 안되면 break
    if count == 4:
        dd = (d + 2) % 4
        lx, ly = r + dx[dd], c + dy[dd]
        if lx < 0 or ly < 0 or lx >= n or ly >= m or board[lx][ly] == 1:
            isBreak = True
        else:
            r, c = lx, ly
            count = 0
print(result)
