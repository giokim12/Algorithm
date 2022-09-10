a = [[3, 5, 9], [4, 2, 1], [1, 1, 5]]

b = [list(map(int, input().split())) for _ in range(3)]
cnt = 0
for i in range(3):
    for j in range(3):
        if b[i][j] == 1:
            cnt += a[i][j]
print(cnt)

