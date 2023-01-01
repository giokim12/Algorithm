'''
5 4 3 9 1
'''

arr = list(map(int, input().split()))
cnt = 0
def dfs(lvl, start, total):
    global cnt

    if 10 <= total <= 20:
        cnt += 1
    elif total >20:
        return

    for i in range(start, len(arr)):
        dfs(lvl+1, i+1, total+arr[i])




dfs(0, 0, 0)
print(cnt)