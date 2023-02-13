def solution(slice, n):
    answer = 0
    answer = int((n-1) / slice) + 1
    return answer

# 2
print(solution(7, 10))
# 3
print(solution(4, 12))