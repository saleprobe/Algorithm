def solution(n, k):
    answer = 0
    service = int(n / 10)
    answer = n * 12000 + k * 2000 - service * 2000
    return answer

# 124000
print(solution(10, 3))
# 768000
print(solution(64, 6))