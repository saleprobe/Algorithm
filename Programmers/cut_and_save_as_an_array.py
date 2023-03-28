# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    count = 0
    buffer = ""
    for s in my_str:
        count += 1
        buffer += s
        if len(buffer)%n == 0:
            answer.append(buffer)
            buffer = ""
        elif len(my_str) == count:
            answer.append(buffer)
    return answer

# ["abc1Ad", "dfggg4", "556b"]
print(solution("abc1Addfggg4556b"))
# ["abc", "def", "123"]
print(solution("abcdef123"))