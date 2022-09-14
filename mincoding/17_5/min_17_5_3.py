name1 = list(map(str, input()))
name2 = list(map(str, input()))

def isSame(name1, name2):
    cnt = 0
    for i in range(len(name1)):
        if name1[i] == name2[i]:
            cnt += 0
        else:
            cnt += 1

        if cnt ==0:
            return 1
        else:
            return 0


if isSame(name1, name2) ==1:
    print('동명')
else:
    print('남남')
