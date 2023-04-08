# 문자열 밀기
def solution(A, B):
    answer = 0
    A = list(A)
    B = list(B)
    while (1):
        if A == B:
            return answer
        A.insert(0, A.pop())
        answer += 1
        if answer >= 100:
            return -1
    return answer

# 1
print(solution("hello", "ohell"))
# -1
print(solution("apple", "elppa"))
# 1
print(solution("atat", "tata"))
# 0
print(solution("abc", "abc"))