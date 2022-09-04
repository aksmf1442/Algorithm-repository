n = int(input())

dp = [0] * (1001)

dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n-1] % 10007)

"""2xn 타일링(dp문제)
    핵심 아이디어: 점화식을 dp[i] = dp[i-1]+ dp[i-2]로 설정하고 풀면 된다.
"""