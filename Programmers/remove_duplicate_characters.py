# 중복된 문자 제거
def solution(my_string):
    answer = ''
    checker = []
    my_string = list(my_string)
    for idx, m in enumerate(my_string):
        if m not in checker:
            checker.append(m)
    answer = ''.join(checker)
    return answer

# "peol"
print(solution("people"))
# "We arthwold"
print(solution("We are the world"))