n = int(input())
candidate = list(map(int, input().split()))

li = []
result = False

for i in candidate:
    while sum(li) > n:
        li.pop(0)
    
    li.append(i)

    if n == sum(li):
        result = True
        break

if result:
    print("여기서부터 여기까지 전부 계산해 주세요!")
else:
    print("다음에 다시 올게요...")