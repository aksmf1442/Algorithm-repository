n = int(input())
dp = [0] * 3

for i in range(n):
    red, green, blue = map(int, input().split())

    dp[0], dp[1], dp[2] = min(dp[1], dp[2]) + red, min(dp[0], dp[2]) + green, min(dp[0], dp[1]) + blue
print(min(dp))
