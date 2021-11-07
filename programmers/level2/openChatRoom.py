# 오픈채팅방

def solution(record):
    answer = []
    result = []
    people = {}
    for man in record:
        arr = man.split(' ')
        if (arr[0] == 'Enter' or arr[0] == 'Change'):
            people[arr[1]] = arr[2]
        
        if (arr[0] == 'Change'):
            continue

        answer.append(arr[0] + ' ' + arr[1])
    
    for state in answer:
        s, id = state.split(' ')
        if (s == 'Enter'):
            result.append(people[id] + "님이 들어왔습니다.")
        
        if (s == 'Leave'):
            result.append(people[id] + "님이 나갔습니다.")
    return result

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))