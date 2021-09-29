n, m = map(int, input().split())
result = []
def dfs(candidate):

    global result

    for i in range(1, n+1):
        if len(candidate) == m:
            break
        candidate.append(i)
        dfs(candidate[:])
        candidate.pop()
    
    if len(candidate) == m:
        result.append(candidate)

dfs([])

for i in result:
    candidate = ""
    for j in i:
        candidate += str(j) + " "
    print(candidate)