n, t = map(int, input().split())

order = list(map(int, input().split())) 

resultCount = 0
result = 0

for i in order:
    if resultCount + i <= t:
        resultCount += i
        result += 1
    else:
        break
    
    if resultCount >= t:
        break

print(result)
            