# 다항식 더하기
def solution(polynomial):
    answer = ''
    num = 0
    num_x = 0
    poly = polynomial.split()
    for p in poly:
        if p != '+':
            if p == 'x':
                num_x += 1
            elif 'x' in p:
                num_x += int(p.replace('x', ''))
            else:
                num += int(p)
    if num_x == 1:
        num_x = ''
    if num != 0 and num_x != 0:
        answer = str(num_x) + 'x' + ' + ' + str(num)
    elif num == 0:
        answer = str(num_x) + 'x'
    elif num_x == 0:
        answer = str(num)
    return answer

# "4x + 7"
print(solution("3x + 7 + x"))
# "3x"
print(solution("x + x + x"))