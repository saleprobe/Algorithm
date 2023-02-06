def solution(sides):
    answer = 2
    max_length = max(sides)
    sides.remove(max_length)
    sum_length = sum(sides)
    if max_length < sum_length:
        answer = 1
    return answer

# 2
print(solution([1, 2, 3]))
# 2
print(solution([3, 6, 2]))
# 1
print(solution([199, 72, 222]))