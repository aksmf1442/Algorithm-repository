n = int(input())

proteinList = [0 for _ in range(3)]

if (n >= 250):
    proteinList[2] = n // 250
    n -= proteinList[2] * 250

if (n >= 40) :
    proteinList[1] = n // 40
    n -= proteinList[1] * 40

if (n >= 10) :
    proteinList[0] = n // 10
    n -= proteinList[0] * 10

if (n > 0):
    print(-1)
else:
    print(" ".join(str(i) for i in proteinList))