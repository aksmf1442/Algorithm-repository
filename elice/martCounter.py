n = int(input())
counter = list(map(int, input().split()))
counter.sort()

candidate = [0 for _ in range(len(counter))]
result = 0

while n >= 1:
    idx = 0
    can = 1000001
    for i in range(len(counter)):
        if (candidate[i] + counter[i]) < can:
            idx = i
            can = candidate[i] + counter[i]
    candidate[idx] += counter[idx]
    n -= 1

candidate.sort()
print(candidate[len(candidate)-1])

# while n >= 1:
#     idx = 0
#     can = 1000001
#     for i in range(len(counter)):
#         if (candidate[i] * counter[i]) < can:
#             idx =  i
#             can = candidate * counter[i]
#     candidate[idx] += 1
#     n -= 1

# for i in range(len(counter)):
#     if result < counter[i] * candidate[i]:
#         result = counter[i] * candidate[i]
# print(result)