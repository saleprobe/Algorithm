# 최빈값 구하기
def solution(array):
    answer = 0
    check = {}
    max_num = -9999
    for num in array:
        if num not in check:
            check[num] = 0
    for num in array:
        check[num] += 1
    for key in check:
        if max_num < check[key]:
            max_num = check[key]
            answer = key
        elif max_num == check[key]:
            answer = -1
    return answer

# 3
print(solution([1, 2, 3, 3, 3, 4]))
# -1
print(solution([1, 1, 2, 2]))
# 1
print(solution([1]))