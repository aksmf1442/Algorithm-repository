n = list(input())
middle = len(n) // 2
left = sum(map(int, n[:len(n)//2]))
right = sum(map(int, n[len(n)//2:]))

if left == right:
    print("LUCKY")
else:
    print("READY")

"""
    파이썬 풀이
    1. 
"""