n, k = map(int, input().split())
result = 0

while n != 1:
    a = n % k
    
    if a != 0:
        n -= a
        result += a
    
    if n != 1:
        n //= k
        result += 1


print(result)