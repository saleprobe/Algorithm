# 진료 순서 정하기
def solution(emergency):
    answer = []
    for value in emergency:
        prio = 1
        for vs in emergency:
            if value < vs:
                prio += 1
        answer.append(prio)
    return answer

# [3, 1, 2]
print(solution([3, 76, 24]))
# [7, 6, 5, 4, 3, 2, 1]
print(solution([1, 2, 3, 4, 5, 6, 7]))
# [2, 4, 3, 5, 1]
print(solution([30, 10, 23, 6, 100]))