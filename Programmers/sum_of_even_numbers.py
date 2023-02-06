def solution(n):
    answer = 0
    for num in range(n+1):
        if num % 2 == 0:
            answer += num
    return answer

# 30
print(solution(10))
# 6
print(solution(4))