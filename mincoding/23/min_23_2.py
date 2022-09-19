arr = list(input())
path = ['']*4
cnt =0
def recur(level):
    global cnt

    if level == 4:
        cnt +=1
        for j in range(1,len(path)):
            if path[j-1]=='K' and path[j]=='B':
                cnt -=1
                break
            elif path[j-1]=='B' and path[j]=='K':
                cnt -=1
                break
            else: continue
        return

    for i in range(len(arr)):
        path[level]=arr[i]
        recur(level+1)


recur(0)
print(cnt)