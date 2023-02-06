def solution(num1, num2):
    answer = 0
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer

# -1
print(solution(2, 3))
# 1
print(solution(11, 11))