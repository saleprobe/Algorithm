# 합성수 찾기
def solution(n):
    answer = 0
    for number in range(1, n+1):
        count = 0
        for num in range(1, number+1):
            if number % num == 0:
                count += 1
        if count >= 3:
            answer += 1
    return answer

# 5
print(solution(10))
# 8
print(solution(15))