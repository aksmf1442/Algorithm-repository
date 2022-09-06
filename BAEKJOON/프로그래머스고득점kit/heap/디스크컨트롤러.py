# 1. 대기중인 작업중에 작업시간이 더 짧은 것을 먼저 처리하면 더 기다리는 평균적으로 기다리는 시간이 더 적다(최소 힙 사용)
# 2. 일단 길이가 가장 짧은 순 기준으로 최소 힙에 넣은 후에 값을 빼고, 뒤에 시작 시간이 time보다 더 늦는다면 다시 대기시키기(while)
import heapq

def solution(jobs):
    q = []
    answer = 0
    [heapq.heappush(q, (i[1], i[0])) for i in jobs]
    times = 0
    progress = 0
    progressStart = 0
    while q or progress != 0:
        if progress == 0:
            answer += (times - progressStart)
            task = 0
            candidate = []
            while task == 0:
                taskLength, start = heapq.heappop(q)
                if start > times:
                    candidate.append((taskLength, start))
                    if not q:
                        [heapq.heappush(q, (i, j)) for i, j in candidate]
                        candidate = []
                        times += 1
                else:
                    task = taskLength
                    progressStart = start

            if candidate:
                [heapq.heappush(q, (i, j)) for i, j in candidate]
            progress = task
        else:
            progress -= 1
            times += 1

    answer += (times - progressStart)
    return answer // len(jobs)

print(solution([[0, 3], [5, 9], [6, 6]]	))