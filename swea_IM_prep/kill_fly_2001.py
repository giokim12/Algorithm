T = int(input())

for tc in range(1, 1+T):
    N , M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    MAX_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            killed_flies = 0
            for k in range(M):
                for l in range(M):
                    killed_flies += arr[i+k][j+l]

            if killed_flies >MAX_kill:
                MAX_kill = killed_flies

    print(f'#{tc} {MAX_kill}')
