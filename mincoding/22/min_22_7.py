find = list(input())
arr=list('ABCD')
path =['']*3
cnt = 0
def recur(level):
    global cnt

    if level==3:
        cnt += 1
        if path == find:
            print(f'{cnt}번째')
        return

    for i in range(len(arr)):
        path[level] = arr[i]
        recur(level+1)


recur(0)

