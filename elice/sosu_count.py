n = int(input())

candidate = []

for num in range(n):
    candidate.append(True)

candidate[0] = False
result = 0
for i in range(1, n+1):

    if (not candidate[i-1]):
        continue

    a = 0

    for j in range(1, i+1):
        if i % j == 0:
            a += 1
        
        if a > 2:
            break
    5
    if a == 2 :
        result +=1

    for j in range(i*2, n+1, i):
        candidate[j-1] = False
    # print(candidate)
    


print(result)

