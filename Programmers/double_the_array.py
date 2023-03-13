# 배열 두 배 만들기
def solution(numbers):
    answer = list(map(lambda x: x * 2, numbers))
    return answer

# [2, 4, 6, 8, 10]
print(solution([1, 2, 3, 4, 5]))
# [2, 4, 200, -198, 2, 4, 6]
print(solution(1, 2, 100, -99, 1, 2, 3))