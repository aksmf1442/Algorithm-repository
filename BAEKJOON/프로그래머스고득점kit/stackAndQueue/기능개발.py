# 1. 뒤에 있는 기능이 먼저 개발 다 되더라도 앞에 있는 기능이 배포될 때 같이 배포됌
# 2. 위의 조건을 지켰을 떄 한 번 배포할 때 몇 개를 같이 배포하는지 리턴
def solution(progresses, speeds):
    answer = []
    idx = 0
    while idx < len(progresses):
        for i in range(len(speeds)):
            if progresses[i] > 100:
                continue
            progresses[i] += speeds[i]
        if progresses[idx] >= 100:
            count = 0
            for i in range(idx, len(progresses)):
                if progresses[i] >= 100:
                    count += 1
                else:
                    break
            answer.append(count)
            idx += count

    return answer

# [2, 1]
print(solution([93, 30, 55], [1, 30, 5]))