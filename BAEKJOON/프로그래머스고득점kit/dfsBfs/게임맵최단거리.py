# 1. bfs 사용해서 최단 거리 찾기
# 2. 만약 도달할 수 없다면 -1출력
from collections import deque


def bfs(x, y, maps):
    queue = deque([(0, 0, 1)])
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    xLength = len(maps)
    yLength = len(maps[0])

    visited = [[0] * len(i) for i in maps]
    visited[x][y] = 1
    result = -1
    while queue:
        x, y, count = queue.popleft()

        if x == xLength - 1 and y == yLength - 1:
            result = count
            break

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if nx < 0 or ny < 0 or nx >= xLength or ny >= yLength:
                continue

            if maps[nx][ny] == 0:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = 1
            queue.append((nx, ny, count + 1))
        print(queue)
    return result

def solution(maps):
    return bfs(0, 0, maps)


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
