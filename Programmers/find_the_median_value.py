# 중앙값 구하기
def solution(array):
    answer = 0
    array = sorted(array)
    answer = array[int(len(array) / 2)]
    return answer

# 7
print(solution([1, 2, 7, 10, 11]))
# 0
print(solution([9, -1, 0]))