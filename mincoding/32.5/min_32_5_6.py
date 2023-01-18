n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = [[0]*n for _ in range(n)]


for i in range(n):
    for j in range(n):
        if m%4 == 1:
            answer[i][j] = arr[n-1-j][n-1-i]
            # answer[i][j] = arr[j][i]
        elif m%4 == 2:
            # answer[i][j] = arr[n-1-i][j]
            answer[i][j] = arr[n-1-i][n-1-j]
        elif m%4 ==3:
            # answer[i][j] = arr[j][n - 1 - i]
            answer[i][j] = arr[j][i]
        else:
            answer[i][j] = arr[i][j]

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')
    print()

