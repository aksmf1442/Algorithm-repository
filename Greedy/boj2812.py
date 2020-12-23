n, k = map(int, input().split())
data = input()
a = n - k
q = []
for i in range(n):
    while q and k > 0 and q[-1] < data[i]:
        q.pop()
        k-=1
    q.append(data[i])
        

print("".join(q[:a]))