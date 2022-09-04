dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs():
    visited.append((i, j))
    queue = [(i, j)]

    while True:
        xx, yy = queue.pop()

        for ii in range(4):
            nx, ny = dx[ii] + xx, dy[ii] + yy
            if nx >= m or nx < 0 or ny >= n or ny < 0:
                continue

            if (nx, ny) in visited or graph[nx][ny] == 0:
                continue
            visited.append((nx, ny))
            queue.append((nx, ny))

        if not queue:
            break

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    visited = []
    result = 0
    for i in range(m):
        for j in range(n):
            if (i, j) in visited or graph[i][j] == 0:
                continue
            bfs()
            result += 1
    print(result)

"""
    파이썬 풀이(bfs를 통한 풀이)
    1. graph를 모두 0으로 초기화하고 배추가 있는 구역은 1로 초기화해준다.
    2. 모든 graph를 방문하면서 배추가 있는 지역을 bfs로 확인하면서 한 번 확인한 곳은 visted에 넣어서 다시 방문할 수 없도록 한다.
    3. bfs를 한 번 돌릴 때 마다 result를 +1 해서 몇 마리의 배추흰지렁이가 필요한지 알아내고 출력한다.
"""