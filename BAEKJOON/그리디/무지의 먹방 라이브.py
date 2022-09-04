import heapq


def solution(food_times, k):
    if (sum(food_times)) < k:
        return -1

    q = []

    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    length = len(food_times)
    sum_value = 0

    while sum_value + (q[0][0] * length) < k:
        sum_value += heapq.heappop(q)[0] * length
        length -= 1

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]


print(solution([8, 6, 4], 15))
