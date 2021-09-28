n = int(input())
counter = list(map(int, input().split()))
counter.sort()

result = 0
left = 1
right = max(counter) * n

while left < right:
    mid = (left + right) // 2
    total = 0
    
    print(left, right, mid)

    for i in counter:
        total += mid // i
    
    if total >= n:
        right = mid
    else:
        left = mid + 1

result = left

print(result)