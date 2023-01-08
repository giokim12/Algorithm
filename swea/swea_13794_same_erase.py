T = int(input())

for tc in range(1, 1+T):
    arr = list(input())


    while True:
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                arr.pop(i)
                arr.pop(i - 1)
                break
        flg = 0
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                flg = 1

        if flg == 0:
            break


    print(f'#{tc} {len(arr)}')