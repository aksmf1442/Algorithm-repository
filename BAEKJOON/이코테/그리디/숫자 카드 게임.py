n, m = map(int, input().split())
result = max(min(list(map(int, input().split()))) for _ in range(n))
print(result)

"""
    파이썬 풀이
    1. 각 행 별로 작은 수를 뽑아서 리스트에 넣고 max()함수를 사용해서 가장 큰 값을 구한다.
"""