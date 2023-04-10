# OX퀴즈
def solution(quiz):
    answer = []
    for q in quiz:
        q = q.split()
        if q[1] == "+":
            cal_val = int(q[0]) + int(q[2])
        else:
            cal_val = int(q[0]) - int(q[2])
        if int(q[4]) == cal_val:
            answer.append("O")
        else:
            answer.append("X")
    return answer

# ["X", "O"]
print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
# ["O", "O", "X", "O"]
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))