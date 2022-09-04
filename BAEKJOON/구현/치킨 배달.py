from itertools import combinations

n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

houses = []
chickenHouse = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            houses.append((i, j))

        if board[i][j] == 2:
            chickenHouse.append((i, j))

chickens = list(combinations(chickenHouse, m))
result = float('inf')
for chicken in chickens:
    minValue = 0
    for houseX, houseY in houses:
        value = float('inf')
        for chickenX, chickenY in chicken:
            value = min(value, abs(houseX - chickenX) + abs(houseY - chickenY))
        minValue += value
    result = min(result, minValue)

print(result)


