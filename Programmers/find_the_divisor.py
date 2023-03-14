# 약수 구하기
def solution(n):
    answer = []
    for check in range(1, n+1):
        if n % check == 0:
            answer.append(check)
    return answer

# [1, 2, 3, 4, 6, 8, 12, 24]
print(solution(24))
# [1, 29]
print(solution(29))