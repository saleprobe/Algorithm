def solution(my_string, letter):
    answer = ''
    answer_list = list(my_string)
    for char in my_string:
        if char == letter:
            answer_list.remove(letter)
    answer = ''.join(answer_list)
    return answer

# "abcde"
print(solution("abcdef", "f"))
# "Cdbe"
print(solution("BCBdbe", "B"))