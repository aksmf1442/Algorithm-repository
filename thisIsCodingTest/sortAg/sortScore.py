n = int(input())
candidate = []

for _ in range(n):
    x, y = input().split()
    candidate.append((x, int(y)))

candidate.sort(key = lambda x : x[1])

[print(i[0], end=" ") for i in candidate]

