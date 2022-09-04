def solution(participant, completion):
    answer = ''
    hashDict = {}
    result = 0

    for man in participant:
        hashDict[hash(man)] = man
        result += hash(man)

    for man in completion:
        result -= hash(man)

    return hashDict[result]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
