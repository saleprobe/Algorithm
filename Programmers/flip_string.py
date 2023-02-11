def solution(my_string):
    answer = ''
    for char in reversed(my_string):
        answer += char
    return answer

# "noraj"
print(solution("jaron"))
# "daerb"
print(solution("bread"))