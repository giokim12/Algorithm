def weird_word(s):
    answer = ''
    answer += s[0].upper()
    print(answer)
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            answer += s[i].upper()
        elif answer[i-1].isupper() == True:
            answer += s[i]
            print(answer)
        else:
            answer += s[i].upper()
            print(answer)
    return answer


weird_word('try hello world')