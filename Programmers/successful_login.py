# 로그인 성공?
def solution(id_pw, db):
    if id_pw in db:
        return 'login'
    for id_pw_s in db:
        if id_pw[0] == id_pw_s[0]:
            return 'wrong pw'
    return 'fail'

# "login"
print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
# "wrong pw"
print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
# "fail"
print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))