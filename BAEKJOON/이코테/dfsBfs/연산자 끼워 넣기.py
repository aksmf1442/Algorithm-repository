def calculate(nums, lst):
    result = nums[0]
    for i in range(len(lst)):
        value = lst[i]
        if value == "+":
            result += nums[i+1]
        if value == "-":
            result -= nums[i+1]
        if value == "*":
            result *= nums[i+1]
        if value == "/":
            result = int(result / nums[i+1])
    return result


def dfs(nums, ops, temp):
    global maxValue, minValue

    if len(ops) == 0:
        result = calculate(nums, temp)
        minValue = min(minValue, result)
        maxValue = max(maxValue, result)
        return

    for i in range(len(ops)):
        opt = ops.pop(i)
        temp.append(opt)
        dfs(nums, ops, temp)
        ops.insert(i, opt)
        temp.pop()
    return


n = int(input())
numList = list(map(int, input().split()))
operatorNums = list(map(int, input().split()))
maxValue = -float('inf')
minValue = float('inf')
operatorList = []
operatorList.extend(["+"] * operatorNums[0])
operatorList.extend(["-"] * operatorNums[1])
operatorList.extend(["*"] * operatorNums[2])
operatorList.extend(["/"] * operatorNums[3])
dfs(numList, operatorList, [])
print(maxValue)
print(minValue)

"""
    파이썬 풀이 - 핵심 아이디어(이 문제를 풀 때 수의 순서는 고정이고, 연산자의 위치만 바꿔서 가장 큰 값과 작은 값을 구한다는 아이디어를 떠올리고 풀어야 한다.)
    1. operatorList와 numList에 값을 초기화해두고 dfs를 돌린다.
    2. dfs를 돌리면서 temp라는 리스트에 연산자를 계속 하나씩 넣어주고 ops(연산자가 들어있는 리스트)가 빈다면 식이 완성됐다고 보고   
    max값과 min값을 초기화해주는 과정을 계속 반복해준다.
    3. 이러한 과정들을 계속들을 계속 반복하다보면 max값과 min값이 나온다.
"""