n = int(input())

money = [500, 100, 50, 10]

result = 0

for m in money :
    s = n // m
    result += s
    n -= s * m

print(result)