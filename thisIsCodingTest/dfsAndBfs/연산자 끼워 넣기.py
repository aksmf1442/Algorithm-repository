def dfs(temp, result, idx):
    global maxValue, minValue
    if len(temp) == 0:
        value = result[0]
        for i in range(len(result)):
            if i % 2 != 0:
                if result[i] == '+':
                    value = value + result[i+1]
                
                if result[i] == '-':
                    value = value - result[i+1]
                
                if result[i] == '*':
                    value = value * result[i+1]
                
                if result[i] == '/':
                    if value < 0:
                        value = -(abs(value) // result[i+1])
                    else:
                        value = value // result[i+1]
        maxValue = max(maxValue, value)
        minValue = min(minValue, value)
        return
    
    for i in range(len(temp)):
        s = temp[i]
        can = temp[:i] + temp[i+1:]
        result.append(s)
        result.append(lis[idx])
        dfs(can, result, idx+1)
        result.pop()
        result.pop()
        
n = int(input())
lis = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
candidate = []
maxValue, minValue = -1000000000, 1000000000
candidate.extend('+' * plus)
candidate.extend('-' * minus)
candidate.extend('*' * multiply)
candidate.extend('/' * divide)

dfs(candidate, [lis[0]], 1)
print(maxValue, minValue)