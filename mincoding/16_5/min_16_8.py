a = [['A', 7, 9, 'T', 'K', 'Q'],
    ['M', 'I', 'N', 'C', 'O', 'D']]

m, n = map(str, input().split())

cnt1 = 0
for i in range(2):
    for j in range(6):
        if a[i][j] == m:
            cnt1 += 1


cnt2 = 0
for i in range(2):
    for j in range(6):
        if a[i][j] == n:
            cnt2 += 1


if cnt1 != 0:
    print(f'{m} : 존재')
else:
    print(f'{m} : 없음')

if cnt2 != 0:
    print(f'{n} : 존재')
else:
    print(f'{n} : 없음')
