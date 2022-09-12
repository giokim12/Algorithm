inp = [list(map(int, input().split())) for _ in range(4)]
arr = [[0]*3 for h in range(4)]

# print(inp)

for i in range(4):
    y = inp[i][0]
    x = inp[i][1]
    arr[y][x] = 5

for m in range(4):
    for n in range(3):
        print(arr[m][n], end =' ')
    print()
