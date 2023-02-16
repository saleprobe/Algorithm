# 외계행성의 나이
def solution(age):
    answer = ''
    age_dic = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'}
    age = str(age)
    for a in age:
        answer += age_dic[a]
    return answer

# "cd"
print(solution(23))
# "fb"
print(solution(51))
# "baa"
print(solution(100))