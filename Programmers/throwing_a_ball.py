# 공 던지기
def solution(numbers, k):
    count = 0
    num = 1
    pre_num = 0
    while (count < k):
        count += 1
        pre_num = num
        num += 2
        if num > len(numbers):
            num = num - len(numbers)
    return pre_num

# 3
print(solution([1, 2, 3, 4], 2))
# 3
print(solution([1, 2, 3, 4, 5, 6], 5))
# 2
print(solution([1, 2, 3], 3))