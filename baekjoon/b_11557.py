T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    MAX = -21e8
    MAX_idx = 0
    for i in range(N):
        arr[i][1] = int(arr[i][1])
        if arr[i][1]>MAX:
            MAX = arr[i][1]
            MAX_idx = i


    print(arr[MAX_idx][0])