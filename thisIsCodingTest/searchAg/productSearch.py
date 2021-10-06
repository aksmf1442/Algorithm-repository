def binary_search(start, end, data, target):
    if start > end:
        return "no"
    
    mid = (start + end) // 2

    if data[mid] == target:
        return "yes"

    if data[mid] > target:
        return binary_search(start, mid - 1, data, target)
    
    if data[mid] < target:
        return binary_search(mid + 1, end, data, target)
    

n = int(input())
candidate = list(map(int, input().split()))
candidate.sort()

m = int(input())
check = list(map(int, input().split()))

for i in check:
    print(binary_search(0, n - 1, candidate, i), end = " ")

