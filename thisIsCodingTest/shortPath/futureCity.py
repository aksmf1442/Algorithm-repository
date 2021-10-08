# 다익스트라 풀이

# import heapq

# n, m = map(int, input().split())
# data = [[] for _ in range(n+1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     data[a].append(b)
#     data[b].append(a)

# x, k = map(int, input().split())
# INF = int(1e9)

# def daikstra(start, end):
#     cop = [INF] * (n + 1)    
    
#     q = []
#     heapq.heappush(q, (0, start))
#     cop[start] = 0

#     while q:
#         dist, now = heapq.heappop(q)

#         if cop[now] < dist:
#             continue

#         for i in data[now]:
#             cost = dist + 1
            

#             if cost < cop[i]:
#                 cop[i] = cost
#                 heapq.heappush(q, (cost, i))
#     return cop[end]

# result = daikstra(1, k) + daikstra(k, x)

# if result <= INF:
#     print(result)
# else:
#     print(-1)



# 플루이드 워셜 풀이

INF = int(1e9)
n, m = map(int, input().split())
data = [[INF] * (n + 1) for _ in range(n+1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            data[a][b] = 0
            data[b][a] = 0

for _ in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1
    data[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            data[a][b] = min(data[a][b], data[a][k] + data[k][b])

distance = data[1][k] + data[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)

