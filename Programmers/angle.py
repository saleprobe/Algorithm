def solution(angle):
    answer = 0
    if angle == 90:
        answer = 2
    elif angle < 90:
        answer = 1
    elif angle == 180:
        answer = 4
    elif angle < 180:
        answer = 3
    return answer

# 1
print(solution(70))
# 3
print(solution(91))
# 4
print(solution(180))