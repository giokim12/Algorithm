arr = list('ABC')
cnt = 0
n = int(input())
path = ['']*n

def recur(level):
    global cnt
    if level==n:
        for j in range(n-2):
            if path[j-2]==path[j-1]==path[j]:
                cnt-=1
                break

        cnt +=1
        return

    for i in range(len(arr)):
            path[level] = arr[i]
            recur(level+1)

recur(0)
print(cnt)