# 7의 개수
def solution(array):
    answer = 0
    for num in array:
        num = str(num)
        for n in num:
            if '7' in n:
                answer += 1
    return answer

# 4
print(solution([7, 77, 17]))
# 0
print(solution([10, 29]))