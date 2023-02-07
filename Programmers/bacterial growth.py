# 세균 증식
def solution(n, t):
    for _ in range(t):
        n *= 2
        answer = n
    return answer

# 2048
print(solution(2, 10))
# 229376
print(solution(7, 15))