# 대문자와 소문자
def solution(my_string):
    answer = ''
    for char in my_string:
        if char.isupper() == True:
            answer += char.lower()
        else:
            answer += char.upper()
    return answer

# "CCCccc"
# "ABcDeFGHij"
print(solution("cccCCC"))
print(solution("abCdEfghIJ"))