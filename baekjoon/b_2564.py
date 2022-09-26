width, height = map(int, input().split())
store_cnt = int(input())
temp = []
for i in range(4):
    temp.append(list(map(int, input().split())))

arr = [[0]*width for _ in range(height)]
for i in range(3):
    if temp[i][0]==1: #북쪽이면
        arr[0][temp[i][1]] = 1
    elif temp[i][0]==2: #남쪽이면
        arr[height-1][temp[i][1]] =1
    elif temp[i][0]==3: #서쪽이면
        arr[temp[i][1]][0]=1
    elif temp[i][0]==4:
        arr[temp[i][1]][width-1]=1

if temp[3][0]==1: #북쪽이면
    arr[0][temp[3][1]] = 2
elif temp[3][0]==2: #남쪽이면
    arr[height-1][temp[3][1]] =2
elif temp[3][0]==3: #서쪽이면
    arr[temp[3][1]][0]=2
elif temp[3][0]==4:
    arr[temp[3][1]][width-1]=2

