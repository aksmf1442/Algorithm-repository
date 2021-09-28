bottleList = []
lidList = []

bottleList.append(int(input()))
bottleList.append(int(input()))
bottleList.append(int(input()))
lidList.append(int(input()))
lidList.append(int(input()))

bottleList.sort()
lidList.sort()

print(bottleList[0] + lidList[0] + 10)
