# 캐릭터의 좌표
def solution(keyinput, board):
    answer = []
    x = 0
    y = 0
    for push in keyinput:
        if push == "left":
            x -= 1
            if abs((board[0] - 1) / 2) < abs(x):
                x += 1
        elif push == "right":
            x += 1
            if abs((board[0] - 1) / 2) < abs(x):
                x -= 1
        elif push == "up":
            y += 1
            if abs((board[1] - 1) / 2) < abs(y):
                y -= 1
        elif push == "down":
            y -= 1
            if abs((board[1] - 1) / 2) < abs(y):
                y += 1
    answer.append(x)
    answer.append(y)
    return answer

# [2, 1]
print(solution(["left", "right", "up", "right", "right"], [11, 11]))
# [0, -4]
print(solution(["down", "down", "down", "down", "down"], [7, 9]))