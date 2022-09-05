#1. 모든 트럭이 다리를 건너는 시간 구하기(초 단위)
#2. 다리에는 최대 bridge_length만큼 올라갈 수 있고, weight이하 무게까지 견디기 가능(and)
#3. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

# 0	[]	[]	[7,4,5,6]
# 1~2	[]	[7]	[4,5,6]
# 3	[7]	[4]	[5,6]
# 4	[7]	[4,5]	[6]
# 5	[7,4]	[5]	[6]
# 6~7	[7,4,5]	[6]	[]
# 8	[7,4,5,6]	[]	[]
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]

    while bridge:

        answer += 1
        bridge.pop(0)

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)

    return answer

print(solution(2, 10, [7,4,5,6]))
