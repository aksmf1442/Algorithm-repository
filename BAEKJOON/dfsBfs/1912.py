n = int(input())
s = list(map(int, input().split()))
sum = [s[0]]

for i in range(n-1):
    sum.append(max(sum[i] + s[i+1], s[i+1]))

print(max(sum))

"""연속합
    핵심 아이디어 : 점화식 max(sum[i] + s[i+1], s[i+1]으로 문제를 풀이
    간략한 설명 
    -> 연속된 수를 선택해서 가장 큰 수를 찾는 문제인데, 이를 생각하고 아이디어를 짜보면 연속된 수를 계속하여 더하다가, 
    sum[i] + s1[i+1]보다 s[i+1]의 값이 더 크다면 이 값을 sum에 append해준다. 이런식으로 아이디어를 생각해보면 
    점화식이 max(sum[i] + s[i+1], s[i+1])이 나온다.
"""