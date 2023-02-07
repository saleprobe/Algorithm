def solution(n):
    answer = []
    for num in range(n+1):
        if num % 2 != 0:
            answer.append(num)
    return answer

# [1, 3, 5, 7, 9]
print(solution(10))
# [1, 3, 5, 7, 9, 11, 13, 15]
print(solution(15))