# 외계어 사전
def solution(spell, dic):
    count = 0
    for word in dic:
        for char in spell:
            if char in word:
                count += 1
        if (len(spell) == count) and (len(spell) == len(word)):
                return 1
        count = 0
    return 2

# 2
print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
# 1
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
# 2
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))