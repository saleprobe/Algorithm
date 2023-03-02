# 숫자 찾기
def solution(num, k):
    answer = -1
    num = list(str(num))
    for idx, value in enumerate(num):
        if value == str(k):
            answer = idx+1
            return answer
    return answer

# 3
print(solution(29183, 1))
# 4
print(solution(232443, 4))
# -1
print(solution(123456, 7))