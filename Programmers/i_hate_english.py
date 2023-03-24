# 영어가 싫어요
def solution(numbers):
    answer = ''
    verse = ''
    for number in numbers:
        verse += number
        if verse == 'zero':
            answer += '0'
            verse = ''
        elif verse == 'one':
            answer += '1'
            verse = ''
        elif verse == 'two':
            answer += '2'
            verse = ''
        elif verse == 'three':
            answer += '3'
            verse = ''
        elif verse == 'four':
            answer += '4'
            verse = ''
        elif verse == 'five':
            answer += '5'
            verse = ''
        elif verse == 'six':
            answer += '6'
            verse = ''
        elif verse == 'seven':
            answer += '7'
            verse = ''
        elif verse == 'eight':
            answer += '8'
            verse = ''
        elif verse == 'nine':
            answer += '9'
            verse = ''
    answer = int(answer)
    return answer

# 123456789
print(solution("onetwothreefourfivesixseveneightnine"))
# 14067
print(solution("onefourzerosixseven"))