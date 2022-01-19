text = input() # 지시사항 1번
print(text.split(','))
start = int(text.split(',')[0])
end = int(text.split(',')[1])
end = min(end, 15)
# 지시사항 4번 구현
for i in range(start, end+1):
    print('*' * i)

