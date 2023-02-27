# 한 번만 등장한 문자
def solution(s):
    answer = []
    answer_dic = {}
    for char in s:
        if char not in answer_dic:
            answer_dic[char] = 1
        elif char in answer_dic:
            answer_dic[char] += 1
    for key, value in answer_dic.items():
        if value == 1:
            answer.append(key)
    answer.sort()
    answer = ''.join(answer)
    return answer

# "d"
print(solution("abcabcadc"))
# "abcd"
print(solution("abdc"))
# "eho"
print(solution("hello"))