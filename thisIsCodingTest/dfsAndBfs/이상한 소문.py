n = int(input())
line_count = int(input())
candidate = [[] for i in range(n+1)]
visited = [0] * (n+1)
result = 0
visited[1] = 1
def dfs(s):
    global result
    
    for i in candidate[s]:
        if visited[i] == 1:
            continue
        
        result += 1
        visited[i] = 1
        dfs(i)
        


for _ in range(line_count):
    x, y = map(int, input().split())
    candidate[x].append(y)
    candidate[y].append(x)
    
dfs(1)
print(result)
