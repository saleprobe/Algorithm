def solution(numbers, num1, num2):
    answer = []
    answer += numbers[num1:num2+1]
    return answer

# [2, 3, 4]
print(solution([1, 2, 3, 4, 5], 1, 3))
# [3, 5]
print(solution([1, 3, 5], 1, 2))