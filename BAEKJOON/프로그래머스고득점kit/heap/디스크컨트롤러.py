# 1. 대기중인 작업중에 작업시간이 더 짧은 것을 먼저 처리하면 더 기다리는 평균적으로 기다리는 시간이 더 적다(최소 힙 사용)
# 2. 일단 길이가 가장 짧은 순 기준으로 최소 힙에 넣은 후에 값을 빼고, 뒤에 시작 시간이 time보다 더 늦는다면 다시 대기시키기(while)
import heapq

def solution(jobs):
    q = []
    times = 0
    answer = 0
    length = len(jobs)
    while jobs or q:
        # 현재 작업할 수 있는 task heapq에 넣기
        removeJobs = []
        for idx, item in enumerate(jobs):
            if item[0] <= times:
                heapq.heappush(q, (item[1], item[0]))
                removeJobs.append(idx)

        for i in reversed(removeJobs):
            jobs.pop(i)

        if q:
            time, start = heapq.heappop(q)
            times += time
            answer += (times - start)
        else:
            times += 1


    return answer // length



print(solution([[0, 3], [1, 9], [2, 6]]	))