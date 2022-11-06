'''
1
9
1 1 3 2 0 0 0 0 0
3 2 5 2 0 0 0 0 0
2 3 3 1 0 0 0 0 0
0 0 0 0 4 5 5 3 1
1 2 5 0 3 6 4 2 1
2 3 6 0 2 1 1 4 2
0 0 0 0 4 2 3 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''
def findmatrix(y, x):
    used[y][x] = 1
    k = 0
    j = 0
    while True:
        k += 1
        nx = x+k
        if nx < N and used[y][nx] == 0 and arr[y][nx] != 0:
            used[y][nx] = 1
        else:
            nx -= 1
            break

    while True:
        j += 1
        ny = y + j
        if ny < N and arr[ny][nx] != 0 and used[ny][nx] == 0:
            used[ny][nx] = 1
        else:
            ny -= 1
            break

    for a in range(y, ny + 1):
        for b in range(x, nx + 1):
            used[a][b] = 1

    result.append([j, k])


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [[0]*N for _ in range(N)]
    cnt = 0
    result = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and used[i][j] == 0:
                cnt += 1
                findmatrix(i, j)

    result = sorted(result, key=lambda x: (x[0] * x[1], x[0]))
    result = sum(result, [])
    print(f'#{tc} {len(result) // 2}', end=" ")

    for i in range(len(result)):
        print(result[i], end=" ")
    print()
