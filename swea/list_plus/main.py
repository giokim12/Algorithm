T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # n명, m초동안 k개
    arr = list(map(int, input().split()))

    bbang_made = [0] * 11112
    cnt = 0
    for i in range(11112):
        if i > 0 and i % M == 0:
            cnt += K
            bbang_made[i] = cnt
        elif bbang_made[i] == 0:
            bbang_made[i] = bbang_made[i - 1]
    print(bbang_made)

    for j in range(len(arr)):
        for l in range(arr[j], len(bbang_made)):
            bbang_made[l] -= 1

    flg = 0
    for k in range(len(bbang_made)):
        if bbang_made[k] < 0:
            flg += 1
    # print(bbang_made)
    # print(flg)

    if flg > 0:
        print(f'#{tc} Impossible')
    else:
        print(f'#{tc} Possible')
