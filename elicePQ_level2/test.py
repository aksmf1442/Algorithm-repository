n = int(input())
answer = input()

blue = "54321"
red = "12345"
yellow = "33333"

length = (n // 5) + 1
blue *= length
red *= length
yellow *= length

blueResult, redResult, yellowResult = 0, 0, 0

for i in range(n):
    if (blue[i]) == answer[i]:
        blueResult += 1
    
    if (red[i]) == answer[i]:
        redResult += 1
    
    if (yellow[i]) == answer[i]:
        yellowResult += 1

maxResult = max(blueResult, redResult, yellowResult)
result = []

if redResult == maxResult:
    result.append("red")

if blueResult == maxResult:
    result.append("blue")

if yellowResult == maxResult:
    result.append("yellow")

print(maxResult)
[print(i) for i in result]