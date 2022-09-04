n = int(input())
s = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if s[j] < s[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

"""가장 긴 증가하는 부분 수열
    핵심 아이디어 : 점화식 max(dp[i], dp[j] + 1)을 통한 풀이
    간략한 설명 
    -> i[:-1]의 값 중에 i번째 값보다 작은 조건을 가진 값 중에서, 가장 긴 값에 +1을 해주는 아이디어를 통해서,
    위와 같은 점화식의 아이디어가 나온다.   
"""