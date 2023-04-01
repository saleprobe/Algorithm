# 치킨 쿠폰
def solution(chicken):
    answer = 0
    while (chicken >= 10):
        answer += (int(chicken // 10))
        chicken = int(chicken / 10) + (chicken % 10)
    return answer

# 11
print(solution(100))
# 120
print(solution(1081))