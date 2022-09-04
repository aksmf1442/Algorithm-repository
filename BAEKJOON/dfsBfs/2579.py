n = int(input())
dp = [0] * 301
s = [0] * 301

for i in range(n):
    s[i] = int(input())

dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[0] + s[2], s[1] + s[2])

for i in range(3, n):
    dp[i] = max(dp[i-3] + s[i] + s[i-1], dp[i-2] + s[i])

print(dp[n-1])

"""계단 오르기(dp문제)
    1. dp와 s에 최대 계단의 개수인 301개를 0으로 다 초기화두고, s에 계단의 점수도 초기화둔다.
    2. 점화식을 사용하기 위해 초기 dp[0, 1, 2]에 값을 초기화해둔다.
    3. max(dp[i-3] + s[i] + s[i-1], dp[i-2] + s[i])의 점화식을 통해 결과값을 도출한다.
"""