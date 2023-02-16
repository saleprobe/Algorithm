# A로 B 만들기
def solution(before, after):
    answer = 0
    before = sorted(before)
    after = sorted(after)
    if before == after:
        return 1
    return answer

# 1
print(solution("olleh", "hello"))
# 0
print(solution("allpe", "apple"))