'''
9
0 1 1 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 1 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

'''

n = int(input())
# name = list(range(n))
arr = [list(map(int, input().split())) for _ in range(n)]
used = [0]*n
answer=[]

def dfs(level):
    global answer

    answer.append(level)

    if len(answer) == 3:
        print(*answer)
        return

    for i in range(n):
        if arr[level][i]==1 and used[i] == 0:
            used[level] = 1
            dfs(i)
            used[level] = 0
            answer.pop()

used[0] = 1
dfs(0)
