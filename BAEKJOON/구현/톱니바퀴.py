circles = []

for _ in range(4):
    circles.append(input())

candidate = [[], [2], [1, 3], [2, 4], [3]]

for _ in range(int(input())):
    current, direction = map(int, input().split())
    visited = [0, 0, 0, 0]
    visited[current - 1] = 1
    possible = [0, 0, 0, 0]
    possible[current - 1] = 1

    for i in candidate[current]:
        if visited[i - 1]:
            continue
        visited[i - 1] = 1
        if current > i and circles[current - 1][6] != circles[i - 1][2]:
            possible[i - 1] = 1
        if current < i and circles[current - 1][2] != circles[i - 1][6]:
            possible[i - 1] = 1

    print(possible)
