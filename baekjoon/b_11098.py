T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    MAX = -21e8
    MAX_idx = 0
    for i in range(N):
        arr[i][0] = int(arr[i][0])
        if arr[i][0]>MAX:
            MAX = arr[i][0]
            MAX_idx = i


    print(arr[MAX_idx][1])