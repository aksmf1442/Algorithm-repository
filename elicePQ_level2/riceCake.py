n = int(input())

check = [True, False, False]

for _ in range(n):
    x, y = map(int, input().split())

    if check[x-1]:
        check[x-1] = False
        check[y-1] = True
    elif check[y-1]:
        check[y-1] = False
        check[x-1] = True

result = 0

for i in range(3):
    if check[i]:
        result = i+1

print(result)