n = int(input())
score_list= []
result = 0
for _ in range(n):
    score_list.append(int(input()))
count = 0
while True:
    is_true = False

    for i in range(1, len(score_list)):
        if score_list[i-1] >= score_list[i]:
            is_true = True;
            result += score_list[i-1] - score_list[i] + 1
            score_list[i-1] -= score_list[i-1] - (score_list[i] - 1)
    if not is_true:
        print(result)
        break