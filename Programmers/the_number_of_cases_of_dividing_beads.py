# 구슬을 나누는 경우의 수
def facto(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    return n * facto(n-1)

def solution(balls, share):
    answer = 0
    answer = int(facto(balls)*((1/facto(balls-share))*(1/facto(share))))
    return answer

# 3
print(solution(3, 2))
# 10
print(solution(5, 3))