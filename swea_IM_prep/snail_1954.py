T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    while Tru