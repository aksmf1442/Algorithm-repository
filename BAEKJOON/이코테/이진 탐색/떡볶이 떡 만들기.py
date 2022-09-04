def binary_search(start, end):
    hap = 0
    mid = ((start + end) // 2) + 1

    for i in lst:
        if i > mid:
            hap += (i - mid)

    if hap == m:
        return mid
    else:
        if hap > m:
            binary_search(mid, end)
        else:
            binary_search(start, mid)

n, m = map(int, input().split())
lst = list(map(int, input().split()))

start = min(lst)
end = max(lst)

result = binary_search(start, end);
print(result)