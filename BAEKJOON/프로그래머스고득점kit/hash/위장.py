def solution(clothes):
    answer = 0
    clothesDict = {}
    for a, b in clothes:
        clothesDict[b] = clothesDict.get(b, 1) + 1

    for i in clothesDict.values():
        answer = i if answer == 0 else answer * i

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
