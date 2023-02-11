def solution(strlist):
    answer = []
    for char in strlist:
        answer.append(len(char))
    return answer

# [2, 3, 3, 6]
print(["We", "are", "the", "world!"])
# [1, 4, 12]
print(["I", "Love", "Programmers."])