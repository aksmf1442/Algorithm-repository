from collections import deque

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]

for i in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1  # 사과 있는 위치에 1로 초기화

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
direction = 0  # 오른쪽: 0, 아래쪽: 1, 왼쪽: 2, 위쪽: 3
result = 0
snakes = deque([[0, 0]])
nx, ny = 0, 0
lst = deque([])


for _ in range(int(input())):
    x, c = input().split()
    x = int(x)
    lst.append((x, c))

x, c = lst.popleft()

while True:
    result += 1
    nx, ny = nx + dx[direction], ny + dy[direction]
    isStop = False

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        isStop = True

    for snake in snakes:
        if [nx, ny] == snake:
            isStop = True
            break

    if isStop:
        break

    if board[nx][ny] == 1:
        board[nx][ny] = 0
        snakes.append([nx, ny])
    elif board[nx][ny] == 0:
        snakes.append([nx, ny])
        snakes.popleft()

    if x == result:

        if c == "D":
            direction = (direction + 1) % 4
        if c == "L":
            direction = (direction - 1) % 4
        if lst:
            x, c = lst.popleft()

print(result)

"""
    파이썬 풀이
    1. board를 0으로 초기화하고 사과가 있는 위치를 1로 초기화한다.
    2. snakes 리스트에 뱀의 현재 위치를 [a, b]로 add해주고, lst에 방향을 전환해야 할 순서를 넣어둔다.
    3. while문을 돌면서 현재 뱀이 움직인 횟수를 result라고 하고 방향을 전환해야 하는 숫자가 x라고 한다면
    x와 result가 같을 경우에 방향을 전환해야 하니까 if x = result를 통해서 방향 전환시 조건을 안에 넣어둔다.
    4. 그렇게 계속 돌다가 뱀이 벽에 마주치거나(if nx < 0 or nx >= n or ny < 0 or ny >= n),
     자신의 꼬리를 잡으면(
     for snake in snakes:
        if [nx, ny] == snake:
            isStop = True
            break
    ) 게임이 종료되고 result를 반환하면 결과가 나온다. 
"""