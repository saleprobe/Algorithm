# 주사위의 개수
def solution(box, n):
    answer = 1
    for index in range(3):
        answer *= (box[index] // n)
    return answer

# 1
print(solution([1, 1, 1], 1))
# 12
print(solution([10, 8, 6], 3))