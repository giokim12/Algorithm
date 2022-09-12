arr = [['_']*5 for h in range(4)]
for k in range(2):
    y, x = map(int, input().split())

    for i in range(8):
        directx = [1, -1, 0, 0, 1, -1, -1, 1]
        directy = [0, 0, 1, -1, -1, 1, -1, 1]

        ny = y + directy[i]
        nx = x + directx[i]

        if ny<0 or nx<0 or nx>4 or ny>3: continue

        arr[ny][nx] = '#'

for m in range(4):
    for n in range(5):
        print(arr[m][n], end= ' ')
    print()