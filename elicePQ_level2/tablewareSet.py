c, s, e = map(int, input().split())

twSet = min([c//2, s])

remainder = ((c//2) - twSet) + (s - twSet)

if (remainder < e):
    candidate = ((e - remainder -1) // 3) + 1
    twSet -= candidate
print(twSet)
