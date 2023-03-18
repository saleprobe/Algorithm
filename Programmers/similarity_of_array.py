# 배열의 유사도
def solution(s1, s2):
    answer = 0
    for front in s1:
        for back in s2:
            if front == back:
                answer += 1
    return answer

# 2
print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
# 0
print(solution(["n", "omg"], ["m", "dot"]))