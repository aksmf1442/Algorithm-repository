def solution(sizes):
    value1 = 0
    value2 = 0
    for size in sizes:
        value1 = max(value1, max(size))
        value2 = max(value2, min(size))
    return value1 * value2

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]	))