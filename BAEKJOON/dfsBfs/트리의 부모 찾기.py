def find(node):
    stack = [node]
    while stack:
        node = stack.pop()
        for currentNode in graph[node]:
            if result[currentNode] != 0:
                continue
            result[currentNode] = node
            stack.append(currentNode)


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = [0] * (n + 1)
result[1] = -1
find(1)

for i in range(2, len(result)):
    print(result[i])
