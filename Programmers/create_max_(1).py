def solution(numbers):
    answer = 0
    first_max = max(numbers)
    numbers.remove(first_max)
    second_max = max(numbers)
    answer = first_max * second_max
    return answer

# 20
print(solution([1, 2, 3, 4, 5]))
# 744
print(solution([0, 31, 24, 10, 1, 9]))