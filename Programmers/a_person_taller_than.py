def solution(array, height):
    answer = 0
    for classmate in array:
        if height < classmate:
            answer += 1
    return answer

# 3
print(solution([149, 180, 192, 170], 167))
# 0
print(solution([180, 120, 140], 190))