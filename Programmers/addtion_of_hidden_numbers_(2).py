# 숨어있는 숫자의 덧셈 (2)
def solution(my_string):
    answer = 0
    stacked_char = '0'
    for char in my_string:
        if char.isdigit():
            stacked_char += char
        else:
            answer += int(stacked_char)
            stacked_char = '0'
    answer += int(stacked_char)
    return answer

# 37
print(solution("aAb1B2cC34oOp"))
# 133
print(solution("1a2b3c4d123Z"))