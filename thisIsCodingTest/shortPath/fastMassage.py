import heapq

n, m, c = map(int, input().split())

INF = int(1e9)
data = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    data[x].append((y, z))

print()
def dikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    
    while q:
        dist, idx = heapq.heappop(q)
        
        if dist > distance[idx]:
            continue
        
        for i in data[idx]:
            idxx, cost = i[0], i[1]
            d = dist + cost
            
            if d < distance[idxx]:
                distance[idxx] = d
                heapq.heappush(q, (d, idxx))

        count = 0
        result = 0
        for i in distance:
            if i != INF:
                count += 1 
                result = max(result, i)
        
        return count, result

a, b = dikstra(c)
print(a, b)