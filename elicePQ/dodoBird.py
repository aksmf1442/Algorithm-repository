n = int(input())
candidate = list(map(int, input().split()))

count = candidate[0]
result = []
result.append(candidate[0])
for i in range(2, n+1):
    a = (i * candidate[i-1]) - count
    count += a
    result.append(a)

print(" ".join(str(i) for i in result))
