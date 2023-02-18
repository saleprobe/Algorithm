# 369게임
def solution(order):
    answer = 0
    order = list(str(order))
    count = 0
    for number in order:
        if number in ['3', '6', '9']:
            count += 1
    answer = count
    return answer

# 1
print(solution(3))
# 2
print(solution(29423))