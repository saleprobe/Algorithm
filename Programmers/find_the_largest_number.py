# 가장 큰 수 찾기
def solution(array):
    answer = []
    max_value = max(array)
    for idx, value in enumerate(array):
        if max_value == value:
            answer.append(max_value)
            answer.append(idx)
    return answer

# [8, 1]
print(solution([1, 8, 3]))
# [11, 2]
print(solution([9, 10, 11, 8]))