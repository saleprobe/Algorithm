# 직사각형 넓이 구하기
def solution(dots):
    answer = 0
    dot_x = []
    dot_y = []
    for dot in dots:
        dot_x.append(dot[0])
        dot_y.append(dot[1])
    answer = (max(dot_x) - min(dot_x)) * (max(dot_y) - min(dot_y))
    return answer

# 1
print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
# 4
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))