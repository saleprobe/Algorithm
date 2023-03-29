# 삼각형의 완성조건 (2)
def solution(sides):
    answer = 0
    for num in range(max(sides)-min(sides)+1, max(sides)+1):
        answer += 1
    for num in range(max(sides)+1, sum(sides)):
        answer += 1
    return answer

# 1
print(solution([1, 2]))
# 5
print(solution([3, 6]))
# 13
print(solution([11, 7]))