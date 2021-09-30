trap = [[] for _ in range(8)]

for i in range(8):
    if i % 2 == 0:
        for _ in range(4):
            trap[i].append(True)
            trap[i].append(False)
    
    if i % 2 != 0:
        for _ in range(4):
            trap[i].append(False)
            trap[i].append(True)

people = []

for i in range(8):
    people.append(list(input()))

result = 0
for i in range(8):
    for j in range(8):
        if trap[i][j] == True and people[i][j] == 'H':
            result += 1

print(result)