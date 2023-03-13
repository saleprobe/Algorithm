# k의 개수
def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        if str(k) in str(num):
            answer += str(num).count(str(k))
    return answer

# 6
print(solution(1, 13, 1))
# 5
print(solution(10, 50, 5))
# 0
print(solution(3, 10, 2))