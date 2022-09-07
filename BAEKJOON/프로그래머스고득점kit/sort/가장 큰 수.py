# 1. 핵심 아이디어는 결국 큰 숫자들이 앞으로 와야 한다(모든 자리수 포함)
# 2. 앞자리가 더 큰 순으로 정렬 그리고 그 다음 숫자가 큰 순으로 정렬(그걸 위해서 *3을 해준다. 1000이하이기 떄문에)
def solution(numbers):
    lst = [str(i) for i in numbers]
    lst.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(lst)))



# 9534330
print(solution([3, 30, 34, 5, 9]))