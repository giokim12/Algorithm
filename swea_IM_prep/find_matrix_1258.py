dy = [1, 0]
dx = [0, 1]

sizes = []
def findmatrix(y, x):
    idx = 0

    nx = x +dx[idx]*j




T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                findmatrix(i, j)

