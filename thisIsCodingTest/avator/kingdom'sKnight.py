dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [1, -1, 2, -2, 2, -2, 1, -1]
location = input()
result = 0


x, y = ord(location[0]) - ord('a'), int(location[1]) - 1

for i in range(8):
    nx, ny = x + dx[i], y + dy[i]

    if nx >= 8 or nx < 0 or ny >= 8 or ny < 0:
        continue
    result += 1

print(result)