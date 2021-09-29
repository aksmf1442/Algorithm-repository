## 피보나치 수열(메모이제이션과 동일, 일정한 규칙을 찾는게 관건)
    
n = int(input())
result = [1, 2]

for i in range(2, n):
    result.append(result[i-2]+result[i-1])

print(result[n-1])