def garo(y, x):



T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            flg+= garo(i, j)+ sero(i, j)+ diag1(i, j)+ diag2(i, j)
    if flg >0:
        print(f"#{tc} YES")
    else:
        print(f'#{tc} NO')




