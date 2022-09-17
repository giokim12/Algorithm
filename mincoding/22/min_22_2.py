word = []

def recur(level):
    a = input()
    word.append(a)

    if level==2:
        if word[level]==word[level-1]==word[level-2]:
            print('WOW')
        elif word[level]!=word[level-1]!=word[level-2]:
            print('BAD')
        else:
            print('GOOD')
        return

    recur(level+1)


recur(0)


