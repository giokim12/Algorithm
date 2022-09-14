accepted = [3, 7, 4, 1, 2, 6]
univer = [list(map(int, input().split())) for _ in range(2)]

def isExist(k):
    cnt = 0
    for i in accepted:
        if i == k:
            cnt += 1
    if cnt>0:
        print('OK', end=' ')
    else:
        print('NO', end= ' ')

for i in range(2):
    for j in range(2):
        isExist(univer[i][j])
    print()

