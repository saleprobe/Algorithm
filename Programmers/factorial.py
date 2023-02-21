# 팩토리얼
def solution(n):
    answer = 0

    def factorial(s):
        if s == 0:
            return 1
        return s * factorial(s - 1)

    num = 1
    while 1:
        if n < factorial(num):
            answer = num - 1
            return answer
        num += 1

# 10
print(solution(3628800))
# 3
print(solution(7))