# 모음 제거
def solution(my_string):
    answer = ''
    for char in my_string:
        if char not in ['a', 'e', 'i', 'o', 'u']:
            answer += char
    return answer

# "bs"
print(solution("bus"))
# "nc t mt y"
print(solution("nice to meet you"))