n = int(input())

candidate = 0

for _ in range(n):
    candidate += int(input())

print(str(candidate)[0:10])