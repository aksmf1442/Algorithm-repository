dp = [0, 1, 1]

for i in range(3, 91):
    dp.append(dp[i-1] + dp[i-2])

n = int(input())
print(dp[n])

"""이친수(dp문제)
    1. dp에 초기값 [0, 1, 1]을 초기화해둔다.
    2. 점화식 dp[i-1] + dp[i-2]를 사용하여 결과값을 도출한다.
"""