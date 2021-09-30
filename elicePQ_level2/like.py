n = int(input())

candidate = []

for _ in range(n):
    candidate.append(list(map(int, input().split())))

candidate.sort(key = lambda x : (x[1], x[0]))

for i in candidate:
    print(" ".join(str(j) for j in i))