# 다음에 올 숫자
def solution(common):
    answer = 0
    if abs(common[0] - common[1]) == abs(common[1] - common[2]):
        answer = common[len(common)-1] + (common[1] - common[0])
    elif common[0] != 1:
        공비 = common[1] - common[0]
        answer = 1
        for _ in range(0, len(common)+1):
            answer = answer * 공비
    else:
        공비 = common[1]
        answer = 1
        for _ in range(0, len(common)):
            answer = answer * 공비
    return answer

# [1, 2, 3, 4]
print(solution(5))
# [2, 4, 8]
print(solution(16))