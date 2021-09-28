n = list(map(int, input().split()))

can = 10000

for i in range(1, len(n)):
    if (can > n[i] - n[i-1]):
        can = n[i] - n [i-1]
    
result = 0    
print(can)
for i in range(1, len(n)):
    if (n[i] - n[i-1] != can):
        result += (n[i] - n[i-1]) // can - 1

print(result)
