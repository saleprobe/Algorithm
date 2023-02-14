# 최댓값 만들기 (2)
def solution(numbers):
    answer = 0
    numbers = sorted(numbers)
    answer = max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
    return answer

# 15
print(solution([1, 2, -3, 4, -5]))
# 240
print(solution([0, -31, 24, 10, 1, 9]))
# 600
print(solution([10, 20, 30, 5, 5, 20, 5]))