# 제곱수 판별하기
import math
def solution(n):
    answer = 2
    if math.sqrt(n) % 1 == 0:
        answer = 1
    return answer

# 1
print(solution(144))
# 2
print(solution(976))