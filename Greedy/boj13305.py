n = int(input())
distance = input().split()
city = input().split()
distance = [int(i) for i in distance]
city = [int(i) for i in city]

oil, result = 0, 0
for i in range(n-1):
    current_pee = city[i]
    if not oil:
        result += current_pee * distance[i]
    else:
        oil -= distance[i]
        continue
    for j in range(i+1, n-1):
        if current_pee < city[j]:
            oil += distance[j]
            result += current_pee * distance[j]
        else:
            break
print(result)