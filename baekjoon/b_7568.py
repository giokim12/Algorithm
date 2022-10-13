N = int(input())
arr= [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    rank = 1
    for j in range(N):
        if arr[j][0]>arr[i][0] and arr[j][1]>arr[i][1]:
            rank +=1

    print(rank, end=' ')
