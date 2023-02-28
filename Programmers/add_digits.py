# 자릿수 더하기
def solution(n):
    answer = 0
    n = str(n)
    for num in n:
        answer += int(num)
    return answer

# 10
print(solution(1234))
# 16
print(solution(930211))