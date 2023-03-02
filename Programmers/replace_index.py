# 인덱스 바꾸기
def solution(my_string, num1, num2):
    answer = ''
    temp = ''
    my_string = list(my_string)
    temp = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = temp
    answer = ''.join(my_string)
    return answer

# "hlelo"
print(solution("hello", 1, 2))
# "I l veoyou"
print(solution("I love you", 3, 6))