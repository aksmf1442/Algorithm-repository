n, m, k = map(int, input().split())
candidate = list(map(int, input().split()))

candidate.sort(key=lambda x : -x)

# 단순한 버전
# while m > 0:
#     if m >= k:
#         result += k * candidate[0]
#         m -= k
    
#     if m == 0:
#         break

#     result += candidate[1]
#     m -= 1

# 복잡한 버전

# a는 반복되는 수열, b는 반복되는 수열중 나머지, c는 1번씩 추가되는 두번째로 큰수
a = (m // (k+1)) * k
b = m % (k+1)
c = (m // (k+1)) * candidate[1]

result = a * candidate[0] + b * candidate[0]
result += c

print(result)