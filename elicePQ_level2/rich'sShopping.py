n, s = map(int, input().split())
goods = list(map(int, input().split()))

result = 100001
candidate = []

while goods:
    if sum(candidate) < s:
        candidate.append(goods.pop(0))
    else:
        while sum(candidate) >= s:
            if len(candidate) < result:
                result = len(candidate)
            candidate.pop(0)
    
while sum(candidate) >= s:
    if len(candidate) < result:
        result = len(candidate)
    candidate.pop(0)

if (result == 100001):
    result = 0

print(result)