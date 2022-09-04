n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

maxValue = lst[-1]
minValue = lst[-2]

count = m // (k + 1)

result = (maxValue * m) - (maxValue * count) + (minValue * count)
print(result)

"""
    파이썬 풀이
    1. 이 문제의 핵심 아이디어는 두 번째로 큰 수를 몇 번 더하는지가 중요하다고 생각했다.
    2. 그래서 규칙을 찾아보니 k번 큰 수를 더하고 1번 두 번째로 큰 수를 더한다는 것을 생각하고 공식을 짜보니  
    m // (k + 1)의 수만큼 두 번째로 큰 수를 더해야 한다는 것을 알았다.
    3. 그리고 최대한 짧게 코드를 짜보고 싶어서 일단 가장 큰 수를 더할 수 있는 만큼 더하고 두 번째로 큰 수를 더해야 하는 만큼
    뺀 후 다시 두 번째로 큰 수를 더해야 하는 만큼 더하는 공식을 짜보니 (maxValue * m) - (maxValue * count) + (minValue * count)
    이런 공식이 나왔고 실제로 저렇게 하면 결과값이 제대로 나온다.
"""