# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    answer = 0
    for char in my_string:
        if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            answer += int(char)
    return answer
# 10
print(solution("aAb1B2cC34oOp"))
# 16
print(solution("1a2b3c4d123"))