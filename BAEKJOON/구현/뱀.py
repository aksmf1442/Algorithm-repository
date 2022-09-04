# 뱀 = 2, 사과 = 1, 아무것도 없음 = 0
# 뱀의 머리가 2 혹은 벽과 부딪히면 게잉 끝
# N의 최대가 100, K의 최대가 100, 방향 횟수 L,

# 보드 크기
n = int(input())

# 게임판
board = [[0] * (n + 1) for _ in range(n + 1)]

# 사과의 개수
k = int(input())

# board에 사과의 위치마다 1로 초기화
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

l = int(input())

# 회전할 방향과 시간 초기화 해두기 (왼쪽 'L', 오른쪽 'D')
direction = []
times = []
for _ in range(l):
    x, c = input().split()
    direction.append(c)
    times.append(int(x))

# 이동한 횟수
result = 0

# 우측부터 시작이라 idx를 0으로 먼저 초기화 해두고, 오른쪽 회전시(D) +1, 왼쪽 회전시(L) -1해준다.
idx = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# 뱀은 1, 1에서 시작
x, y = 1, 1
snakeBody = [(x, y)]

while True:
    # 이동할 방향
    nx, ny = x + dx[idx], y + dy[idx]
    result += 1

    # 벽에 부딪히거나 자신의 몸에 닿으면 반복문을 빠져나가기
    if nx <= 0 or nx > n or ny <= 0 or ny > n or (nx, ny) in snakeBody:
        break

    # 뱀의 머리가 사과와 마주치지 않을 경우 snakeBoby의 꼬리 부분을 빼준다(pop(0))
    if board[nx][ny] != 1:
        snakeBody.pop(0)
    else:
        board[nx][ny] = 0

    # 회전할 때가 되면 방향에 맞게 회전 시켜준다.
    if result in times:
        d = direction.pop(0)
        if d == "L":
            idx = (idx - 1) % 4

        if d == "D":
            idx = (idx + 1) % 4

    snakeBody.append((nx, ny))
    x, y = nx, ny

print(result)
