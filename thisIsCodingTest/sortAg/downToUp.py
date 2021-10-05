n = int(input())
candidate = []
for _ in range(n):
    candidate.append(int(input()))

candidate.sort(key = lambda x : -x)

print(" ".join([str(i) for i in candidate]))