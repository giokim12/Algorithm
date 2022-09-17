passwords = ['Jason', 'Dr.tom', 'EXEXI', 'GK12P', 'POW']
pwd = input()
cnt = 0
def recur(level):
    global cnt
    if level==5:
        if cnt>0:
            print('암호해제')
        else:
            print('암호틀림')
        return

    if passwords[level]==pwd:
        cnt +=1
    recur(level+1)
recur(0)