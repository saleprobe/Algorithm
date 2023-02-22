# 개미 군단
def solution(hp):
    answer = 0
    ge, so, wo = 0, 0, 0
    ge = int(hp / 5)
    so = int((hp % 5) / 3)
    wo = int(((hp % 5) % 3) / 1 )
    answer = ge + so + wo
    return answer

# 5
print(solution(23))
# 6
print(solution(24))
# 201
print(solution(999))