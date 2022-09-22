from collections import defaultdict


def solution(n, results):
    answer = 0
    graph = [[0] * n for _ in range(n)]

    for winner, loser in results:
        graph[winner - 1][loser - 1] = 1
        graph[loser - 1][winner - 1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or graph[i][j] in [1, -1]:
                    continue

                if graph[i][k] == graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = graph[k][i] = graph[j][k] = -1

    for n in graph:
        if n.count(0) == 1:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))