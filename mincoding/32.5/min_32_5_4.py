n = int(input())
arr = [list(input().split()) for _ in range(n)]

flg = 0
min_top = 50
max_bottom = 1
for i in range(n):
    arr[i][0] = int(arr[i][0])
    if arr[i][1] == 'DOWN' and arr[i][0]<=min_top:
        min_top = arr[i][0]-1

    if arr[i][1] == 'UP' and arr[i][0]>=max_bottom:
        max_bottom = arr[i][0]+1


    if min_top == max_bottom:
        flg = 1
        print(min_top)

if flg == 0:
    if max_bottom>min_top:
        print('ERROR')
    else:
        print(f'{max_bottom} ~ {min_top}')
