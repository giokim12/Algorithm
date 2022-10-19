N = int(input())
#1일때 1
#2일때 5
#3일때 9
#4일때 13
arr = [[' ']*(4*N-3) for _ in range(4*N-3)]
M = 4 * N - 3
def rcr(n, y, x):
    M1 = 4*n-3
    if n <= 0:
        return

    for i in range(y, y+M1):
        for j in range(x, x+M1):
            if i == y or j == x or i== M1+y-1 or j == M1+x-1:
                arr[i][j] = '*'

    rcr(n-1, y+2, x+2)


rcr(N, 0, 0)

for i in range(M):
    for j in range(M):
        print(arr[i][j], end= '')
    print()

