input_data = input()
input_list = [int(i) for i in input_data.split(',')] # 입력값을 정수의 리스트로 변환
resid_list = []
# 지시사항에 따라 처리한 리스트( 각 요소는 정수)

for i in range(len(input_list) - 1):
    resid_list.append(input_list[i+1] - input_list[i])

count1 = 0
count2 = 0
for i in range(len(input_list)):
    count1 += resid_list[i]
    count2 += input_list[i]
    
print(count1)
print(count2)

# 원본이 1이 많으면
print(input_list)
# 바뀐 형식이 1이 많으면
print(resid_list)
# 1의 수가 같으면
print(0)
