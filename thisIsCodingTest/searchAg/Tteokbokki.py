n, m = map(int, input().split())

def binary_search(start, end, candidate, target):
    mid = (start + end) // 2
    result = 0
    for i in candidate:
        if i > mid:
            result += (i - mid)
    
    if result == target:
        return mid
    
    if result > target:
        return binary_search(mid + 1, end, candidate, target)
    
    if result < target:
        return binary_search(start, mid - 1, candidate, target)
    
    


data = list(map(int, input().split()))
minLength = min(data)
maxLength = max(data)

print(binary_search(minLength, maxLength, data, m))