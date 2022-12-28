arr = [[0, 0, 1, 0, 1, 1],
       [1, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]
       ]

start, end = map(int, input().split())
used = [0]*6
minCnt = 21e8
cnt = 0

def dfs(lvl):
    global minCnt, cnt

    if lvl == end-1:
        if cnt<minCnt:
            minCnt = cnt
            return


    for i in range(6):
        if used[i] ==0 and arr[lvl][i] == 1:
            used[i] = 1
            cnt +=1
            dfs(i)
            used[i] = 0
            cnt -=1



dfs(start-1)
if minCnt == 21e8:
    print(0)
else:
    print(minCnt)