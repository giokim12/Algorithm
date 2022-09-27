a, b = map(int, input().split())

arr = [[0]*3 for _ in range(2)]

for j in range(3):
    arr[0][j] = a
    arr[1][j] = b

for _ in range(3):
    for i in range(2):
        for j in range(3):
            print(arr[i][j], end= ' ')
        print()
    print()