letters = list(input())
# print(letters)
arr = [list(map(int, input().split())) for _ in range(len(letters))]

answer=[]
def dfs(now):
    global answer
    answer.append(letters[now])

    for i in range(len(letters)):
        if arr[now][i]==1:
            dfs(i)

dfs(0)
for i in range(len(answer)):
    print(answer[i], end='')