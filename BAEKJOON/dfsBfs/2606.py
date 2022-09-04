cpt = int(input())
cptLine = int(input())
cptGraph = [[] for _ in range(cpt + 1)]

for i in range(cptLine):
    a, b = map(int, input().split())
    cptGraph[a].append(b)
    cptGraph[b].append(a)


def bfs():
    print(cptGraph)
    visited = []
    visited.append(1)
    queue = [1]
    n = queue.pop(0)
    while True:
        for c in cptGraph[n]:
            if c in visited:
                continue
            queue.append(c)
            visited.append(c)

        if len(queue) == 0:
            break

        n = queue.pop(0)
    print(len(visited) - 1)

bfs()
"""
    파이썬 풀이(bfs를 통한 풀이)
    1. 서로 참조하는 모든 값을 cptGraph에 리스트 방식으로 넣는다.
    2. queue에 바이러스에 감염된(연결된) 값들을 계속 넣어주면서 visted와 queue에 감염된 컴퓨터를 append한다.
    3. bfs 기법으로 반복하다가 더이상 감염시킬 컴퓨터가 없다면 break하고 visited의 길이 - 1의 값을 결과값으로 낸다.
"""
