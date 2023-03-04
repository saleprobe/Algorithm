# 피자 나눠 먹기 (2)
def solution(n):
    answer = 0
    num = 1
    while 1:
        if (6 * num) / n == int((6 * num) / n):
            answer = num
            return answer
        num += 1


# 1
print(solution(6))
# 5
print(solution(10))
# 2
print(solution(4))