n = int(input())
dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)


print(dp[n])

"""1로 만들기(dp문제)
    1. dp에 0으로 다 초기화해둔다.
    2. 메모이제이션을 통해서 dp에 n까지의 최솟값을 저장해둔다.
    (이 때 모든 경우의 수를 고려해야 해서 3으로 나눌 떄, 2로 나눌 때, +1할 때를 다 고려한다.
    3. dp[n]을 출력한다.
"""