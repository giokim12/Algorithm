T = int(input())

for tc in range(1, 1+T):
    n = int(input())
    arr = list(input().split())

    result = []

    shuffle_bottom = arr[:((n-1)//2)+1]
    shuffle_top = arr[((n-1)//2)+1: ]

    while shuffle_bottom:
        a = shuffle_bottom.pop(0)
        result.append(a)
        if shuffle_top:
            b = shuffle_top.pop(0)
            result.append(b)



    print(f'#{tc}', end=' ')
    for i in range(len(result)):
        print(result[i], end=' ')
    print()



