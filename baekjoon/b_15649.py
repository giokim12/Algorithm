N, M = map(int, input().split())
arr = list(range(1, N+1))
used = [0]*N
path = [0]*M
def rcr(level):

    if level == M:
        print(*path)
        return

    for i in range(N):
        if used[i] == 1:
            continue
        used[i] = 1
        path[level]=arr[i]
        rcr(level+1)
        path[level] = 0
        used[i] = 0

rcr(0)