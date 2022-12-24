n = int(input())
name = list(range(n))

arr = [list(map(int, input().split())) for _ in range(n)]

answer=[]
def dfs(now):
    global answer
    answer.append(name[now])
    for i in range(n):
        if arr[now][i]==1:
            dfs(i)

dfs(0)
print(*answer)
