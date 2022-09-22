from _heapq import heappop, heappush

graph = []
INF = int(1e9)


def initGraph(n, fares):
    global graph
    graph = [[] for _ in range(n + 1)]

    for x, y, value in fares:
        graph[x].append((y, value))
        graph[y].append((x, value))


def dikstra(start, end):
    result = [INF] * len(graph)
    queue = [(0, start)]
    result[start] = 0

    while queue:
        dt, start = heappop(queue)

        for node, value in graph[start]:
            ncount = dt + value
            if ncount >= result[node]:
                continue
            result[node] = ncount
            heappush(queue, (ncount, node))

    return result[end]


def solution(n, s, a, b, fares):
    initGraph(n, fares)
    result = INF
    for i in range(1, n + 1):
        result = min(result, dikstra(s, i) + dikstra(i, a) + dikstra(i, b))
    return result


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
