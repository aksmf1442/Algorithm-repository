import heapq

n, m = map(int, input().split())
data = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

x, k = map(int, input().split())
INF = int(1e9)

def daikstra(start, end):
    cop = [INF] * (n + 1)    
    
    q = []
    heapq.heappush(q, (0, start))
    cop[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if cop[now] < dist:
            continue

        for i in data[now]:
            cost = dist + 1
            

            if cost < cop[i]:
                cop[i] = cost
                heapq.heappush(q, (cost, i))
    return cop[end]

result = daikstra(1, k) + daikstra(k, x)

if result <= INF:
    print(result)
else:
    print(-1)







