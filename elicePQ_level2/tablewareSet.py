c, s, e = map(int, input().split())

twSet = min([c//2, s])

remainder = ((c//2) - twSet) + (s - twSet) // 2

if (remainder < e):
    twSet -= (e - remainder)

print(twSet)
