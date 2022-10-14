T = int(input())

for tc in range(1, 1+T):
    N, M, K = map(int, input().split()) #손님 수, M초 마다 K개씩
    arr = list(map(int, input().split()))
    # arr = sorted(arr, key=lambda x: x)
    # print(arr)

    bbang_made = 0
    flg = 0
    for seconds in range(11112):
        if seconds > 0 and seconds % M == 0:
            bbang_made += K
        for visits in range(len(arr)):
            if arr[visits] == seconds:
                bbang_made -=1

            if bbang_made<0:
                flg = 1
                break


    if flg ==1:
        print(f'#{tc} Impossible')
    else:
        print(f'#{tc} Possible')

