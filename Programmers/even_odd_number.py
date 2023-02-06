def solution(num_list):
    answer = []
    even, odd = 0, 0
    for num in num_list:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    answer.append(even)
    answer.append(odd)
    return answer

# [2, 3]
print(solution([1, 2, 3, 4, 5]))
# [0, 4]
print(solution([1, 3, 5, 7]))