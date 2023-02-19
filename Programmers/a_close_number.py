# 가까운 수
def solution(array, n):
    answer = 0
    array.sort(key = lambda x: abs(n-x))
    if abs(array[0]-n) == abs(array[1]-n) and array[0] > array[1]:
        answer = array[1]
        return answer
    answer = array[0]
    return answer

# 28
print(solution([3, 10, 28]))
# 12
print(solution([10, 11, 12]))