def solution(num1, num2):
    answer = 0
    answer = int((num1 / num2) * 1000)
    return answer

# 1500
print(solution(3, 2))
# 2333
print(solution(7, 3))
# 62
print(solution(1, 16))