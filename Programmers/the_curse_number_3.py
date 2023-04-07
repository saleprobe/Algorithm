# 저주의 숫자 3
def solution(n):
    answer = []
    num = 0
    while (1):
        num += 1
        if '3' not in str(num) and num % 3 != 0:
            answer.append(num)
        if len(answer) == n:
            return answer[n - 1]


# 25
print(solution(15))
# 76
print(solution(40))