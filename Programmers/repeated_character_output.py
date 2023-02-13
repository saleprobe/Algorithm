def solution(my_string, n):
    answer = ''
    for char in my_string:
        answer = answer + char * n
    return answer

# "hhheeellllllooo"
print(solution("hello", 3))