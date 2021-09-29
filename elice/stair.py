def dfs(li):
    if sum(li) == n:
        global result
        result += 1
        return

    if sum(li) > n:
        return
    
    for i in range(1, 3):
        li.append(i)
        dfs(li)
        li.pop()
    

n = int(input())
result = 0
dfs([])
print(result)