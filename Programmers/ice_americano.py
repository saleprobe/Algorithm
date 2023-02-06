def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money % 5500)
    return answer

# [1, 0]
print(solution(5500))
# [2, 4000]
print(solution(15000))