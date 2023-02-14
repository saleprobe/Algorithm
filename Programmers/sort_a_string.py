# 문자열 정렬하기 (2)
def solution(my_string):
    answer = ''
    aa = my_string.lower()
    my_string = sorted(my_string.lower())
    answer = ''.join(my_string)
    return answer

# "abcd"
print(solution("Bcad"))
# "ehllo"
print(solution("heLLo"))
# "hnopty"
print(solution("Python"))