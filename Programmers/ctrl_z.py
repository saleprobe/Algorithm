# 컨트롤 제트
def solution(s):
    answer = 0
    s = s.split()
    before_word = 0
    for word in s:
        if word == 'Z':
            answer -= int(before_word)
            before_word = 0
        elif word != 'Z':
            answer += int(word)
            before_word = int(word)

    return answer

# 4
print(solution("1 2 Z 3"))
# 100
print(solution("10 20 30 40"))
# 1
print(solution("10 Z 20 Z 1"))
# 0
print(solution("10 Z 20 Z"))
# -3
print(solution("-1 -2 -3 Z"))