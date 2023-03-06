# 가위 바위 보
def solution(rsp):
    answer = ''
    for victim in rsp:
        if victim == '2':
            answer += '0'
        elif victim == '0':
            answer += '5'
        else:
            answer += '2'
    return answer

# "0"
print(solution("2"))
# "052"
print(solution("205"))