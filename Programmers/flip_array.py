def solution(num_list):
    answer = []
    for num in reversed(num_list):
        answer.append(num)
    return answer

# [5, 4, 3, 2, 1]
print(solution([1, 2, 3, 4, 5]))
# [2, 1, 1, 1, 1, 1]
print(solution([1, 1, 1, 1, 1, 2]))
# [5, 3, 1, 1, 1, 0, 1]
print(solution([1, 0, 1, 1, 1, 3, 5]))