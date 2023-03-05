# 모스부호 (1)
morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
def solution(letter):
    answer = ''
    letter = letter.split()
    for m in letter:
        answer += morse[m]
    return answer

# "hello"
print(solution(".... . .-.. .-.. ---"))
# "python"
print(solution(".--. -.-- - .... --- -."))