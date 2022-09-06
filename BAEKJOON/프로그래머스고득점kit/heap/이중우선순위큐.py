# 1. 최대값 큐, 최소값 큐를 따로 만들고 두 번째 인자로 리스트의 인덱스를 넣어줘서 실제로 지울 땐 임의의 리스트에서 지우기
# 2. 결국 만들어야 할 자료구조는 큐 2개, 리스트 1개
import heapq
def solution(operations):
    answer = [0, 0]
    minHeapQ = []
    maxHeapQ = []
    candidate = []
    removeCandidate = []
    visited = [0] * 1000001
    count = 0
    for idx, item in enumerate(operations):
        value = item.split(" ")
        if value[0] == "I":
            candidate.append(int(value[1]))
            heapq.heappush(minHeapQ, (int(value[1]), len(candidate) - 1))
            heapq.heappush(maxHeapQ, (-int(value[1]), len(candidate) - 1))
            count += 1

        if count == 0:
            continue

        if value[0] == "D" and value[1] == "-1":
            num, i = heapq.heappop(minHeapQ)
            while visited[i]:
                num, i = heapq.heappop(minHeapQ)
            visited[i] = 1
            removeCandidate.append(i)
            count -= 1

        if value[0] == "D" and value[1] == "1":
            num, i = heapq.heappop(maxHeapQ)
            while visited[i]:
                num, i = heapq.heappop(maxHeapQ)
            visited[i] = 1
            removeCandidate.append(i)
            count -= 1

    removeCandidate.sort(key=lambda x: -x)

    for i in removeCandidate:
        candidate.pop(i)

    if candidate:
        candidate.sort()
        answer = [candidate[-1], candidate[0]]
    return answer


# [0, 0]
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))

# [333, -45]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))