def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x



n = list(map(int, input().split()))

can = n[0]

for i in range(1, len(n)):
    can = gcd(can, n[i])

result = 0    
print(can)
for i in range(1, len(n)):
    if (n[i] - n[i-1] != can):
        result += (n[i] - n[i-1]) // can - 1

print(result)
