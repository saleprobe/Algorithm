# 배열 회전시키기
def solution(numbers, direction):
    answer = []
    tepm = ''
    if direction == "right":
        numbers.insert(0, numbers[len(numbers)-1])
        numbers.pop(len(numbers)-1)
        answer = numbers
    else:
        numbers.append(numbers[0])
        numbers.pop(0)
        answer = numbers
    return answer

# [3, 1, 2]
print(solution([1, 2, 3], "right"))
# [455, 6, 4, -1, 45, 6, 4]
print(solution([4, 455, 6, 4, -1, 45, 6]))
# deque 사용 요망