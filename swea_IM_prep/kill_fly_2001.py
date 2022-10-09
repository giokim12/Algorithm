T = int(input())

for tc in range(1, 1+T):
    N , M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N-M):
        for j in range(N-M):
            for k in range(M):
