dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
n, m = map(int, input().split())
x, y, idx = map(int, input().split())
gameMap = []
result = 1

for _ in range(n):
    candidate = list(map(int, input().split()))
    gameMap.append(candidate)

gameMap[x][y] = 1
count= 0

while True:
    nx, ny = x + dx[idx], y + dy[idx]
    
    if  nx < 0 or nx >= n or ny < 0 or ny >= m or gameMap[nx][ny] == 1:
        idx = (idx + 1) % 4
        count += 1

        if count == 4:
            break

        continue
    
    gameMap[nx][ny] = 1
    result +=1
    x, y = nx, ny
    count = 0
print(result)