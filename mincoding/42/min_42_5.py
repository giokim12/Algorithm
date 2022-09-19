arr = list(range(1, 10))
n = int(input())
cnt = 0

def rcr(lvl, total):
    global cnt

    if lvl == n:
        if total==10:
            cnt+=1
        return

    for i in range(len(arr)):
        rcr(lvl+1, total+arr[i])

rcr(0, 0)
print(cnt)