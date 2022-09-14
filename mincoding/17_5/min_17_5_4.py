tr = [['G','K','T'], ['P','A','C']]
exi = list(map(str, input().split()))
a = []
def isExist(k):
    for i in range(2):
        for j in range(3):
            if tr[i][j] == k:
                return 1
    return 0

cnt = 0
for i in range(2):
    a.append(isExist(exi[i]))
    cnt += a[i]


if cnt == 2:
    print("대발견")
elif cnt ==1:
    print("중발견")
else:
    print("미발견")