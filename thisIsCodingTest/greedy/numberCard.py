n, m = map(int, input().split())
cardList = []

for _ in range(n):
    cardList.append(list(map(int, input().split())))

result = max([min(i) for i in cardList])
print(result)