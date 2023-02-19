# 암호 해독
def solution(cipher, code):
    answer = ''
    for num in range(1, len(cipher)+1):
        if num % code == 0:
            answer += cipher[num-1]
    return answer

# "attack"
print(solution("dfjardstddetckdaccccdegk", 4))
# "fallback"
print(solution("pfqallllabwaoclk", 2))