a = []
cnt = 0
for i in range(7):
    a.append([])
    for j in range(4):
        cnt += 1
        a[i].append(cnt)

n1, n2, n3 = map(int, input().split())

for i in range(7):
    for j in range(4):
        a[n1][j] =0
        a[n2][j] = 0
        a[n3][j] = 0

for i in range(7):
    for j in range(4):
        print(a[i][j], end= ' ')
    print()
