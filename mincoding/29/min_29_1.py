n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = []
def dfs(level):

    answer.append(level)

    if len(answer) == n:
        return

    for i in range(n):
        if arr[level][i] == 1:
            dfs(i)




dfs(0)
print(*answer)