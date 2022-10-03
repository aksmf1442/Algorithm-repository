# goal: 뭉쳐 있는 나라들끼리 세력이 큰 나라가 나머지 나라의 영토를 갖는다.
# 1. 지도에 여러 나라가 표시되어 있고, 알바펫 대문자로 구별됩니다.
# 2. 빈 영토는 흰색, 한나라는 한 덩어리로 붙어 있을 수도 있고,
#   여러 덩어리로 떨어져 있을 수도 있습니다.
# 3. 한 덩어리로 붙어있는 나라들끼리 전쟁중이며 세력이 큰 나라가 승리합니다.
#   기준: 1. 세력이 강한 기준은 알파벳이 많은 나라
#        2. 세력이 같으면 알파벳 순서가 가장 뒤인 나라(A,Z라면 Z)
#        3. 하지만 세력이 약한 부분만 뺏는거고 같으면 그대로 두기

# 풀이 순서
# 1. 각 싸움중인 영토에서 dic으로 A:1, B:2처럼 몇 개의 영토를 가졌는지 확인
# 2. 확인하면 가장 세력이 큰 나라로 dfs를 사용해서 덮어버리기
import sys
sys.setrecursionlimit(100000)
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
N, M = 0, 0


def warCount(x, y, maps, visited, warDic):
    if visited[x][y] != 0:
        return
    visited[x][y] = 1
    country = maps[x][y]

    if country not in warDic:
        warDic[country] = 1
    else:
        warDic[country] += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if maps[nx][ny] == ".":
            continue

        warCount(nx, ny, maps, visited, warDic)


def replaceMap(x, y, maps, warDic, country, visited, maxValue):
    if visited[x][y] != 1:
        return

    if warDic[maps[x][y]] != maxValue:
        maps[x][y] = country

    visited[x][y] += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if maps[nx][ny] == ".":
            continue

        replaceMap(nx, ny, maps, warDic, country, visited, maxValue)


def solution(maps):
    global N, M
    maps = [list(country) for country in maps]
    N, M = len(maps), len(maps[0])
    visited = [[0] * M for _ in range(N)]

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != "." and visited[i][j] == 0:
                # 1. 각 싸움중인 영토에서 dic으로 A:1, B:2처럼 몇 개의 영토를 가졌는지 확인
                warDic = {}
                warCount(i, j, maps, visited, warDic)
                maxValue = max(warDic.values())
                candidate = []
                for a, count in warDic.items():
                    if count == maxValue:
                        candidate.append(a)
                candidate.sort()

                # 2. 세력이 적은 영토를 세력이 강한 영토가 차지하기
                replaceMap(i, j, maps, warDic, candidate[-1], visited, maxValue)
    result = {}
    for i in range(N):
        for j in range(M):
            if maps[i][j] == ".":
                continue
            if maps[i][j] not in result:
                result[maps[i][j]] = 1
            else:
                result[maps[i][j]] += 1
    return max(result.values())


# 15
print(solution(
    ["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]))
