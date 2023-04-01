# 소인수분해
def solution(n):
    answer = []
    box = []
    count = 0
    for num in range(2, 10001):
        for solid in range(1, num+1):
            if num % solid == 0:
                count += 1
        if count == 2:
            box.append(num)
        count = 0
    for num in box:
        if n % num == 0:
            answer.append(num)
    if answer == []:
        answer.append(n)
    return answer

# [2, 3]
print(solution(12))
# [17]
print(solution(17))
# [2, 3, 5, 7]
print(solution(420))