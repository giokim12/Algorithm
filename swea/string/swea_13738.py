T = int(input())

for tc in range(1, T+1):
    short = list(input())
    long = list(input())

    def findPattern(idx):
        for i in range(len(short)):
            if long[idx+i] != short[i]:
                return 0
        return 1

    flg = 0
    for k in range(len(long)-len(short)+1):
        flg += findPattern(k)

    if flg >=1:
        flg =1

    print(f'#{tc} {flg}')
