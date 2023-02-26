# 이진수 더하기
def solution(bin1, bin2):
    answer = ''
    bin1 = '0b' + bin1
    bin2 = '0b' + bin2
    plus_bin = int(bin1, 2) + int(bin2, 2)
    answer = bin(plus_bin)[2:]
    return answer

# "101"
print(solution("10", "11"))
# "11000"
print(solution("1001", "1111"))