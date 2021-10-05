n, k = map(int, input().split())
data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

while k > 0:
    mindata = min(data1)
    maxData = max(data2)
    idx1 = data1.index(mindata)
    idx2 = data2.index(maxData)
    
    if mindata >= maxData:
        break

    data1[idx1] = maxData
    data2[idx2] = mindata
    k -= 1

print(sum(data1))
    