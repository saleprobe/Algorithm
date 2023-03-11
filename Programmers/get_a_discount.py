# 옷가게 할인 받기
def solution(price):
    answer = 0
    if price >= 500000:
        answer = int(price * 0.8)
    elif price >= 300000:
        answer = int(price * 0.9)
    elif price >= 100000:
        answer = int(price * 0.95)
    else:
        answer = price
    return answer
# 142500
print(solution(150000))
# 464000
print(solution(580000))