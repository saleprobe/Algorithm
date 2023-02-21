# 문자열 정렬하기 (1)
def solution(my_string):
    answer = []
    for char in my_string:
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            answer.append(int(char))
            answer = sorted(answer)
    return answer

# [1, 2, 2, 3, 9]
print(solution("hi12392"))
# [2, 2, 4, 8]
print(solution("p2o4i8gj2"))
# [0]
print(solution("abcde0"))