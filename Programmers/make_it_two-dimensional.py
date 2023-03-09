# 2차원으로 만들기
def solution(num_list, n):
    answer = []
    temp = []
    for idx in range(len(num_list)):
        temp.append(num_list[idx])
        if len(temp) == n:
            answer.append(temp)
            temp = []
    return answer

# [[1, 2], [3, 4], [5, 6], [7, 8]]
print(solution([1, 2, 3, 4, 5, 6, 7, 8]))
# [[100, 95, 2], [4, 5, 6], [18, 33, 948]]
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948]))