# 1. 스코빌 지수를 K이상
# 2. 위의 조건을 위해서는 [섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)]의 방법으로 새로운 음식을 만듬.
# 3. 모든 음식의 스코빌 지수가 K이상이 될 때까지 위의 과정을 반복
import heapq


def solution(scoville, K):
    answer = 0
    q = []
    # 모든 원소를 최소 힙에 넣어준다.
    [heapq.heappush(q, i) for i in scoville]
    isPossible = False
    while len(q) >= 1:
        first = heapq.heappop(q)
        if first >= K:
            isPossible = True
            break
        if len(q) == 0:
            break
        second = heapq.heappop(q)
        heapq.heappush(q, first + (second * 2))
        answer += 1

    return answer if isPossible else -1


print(solution([1, 2, 3, 9, 10, 12], 7))
