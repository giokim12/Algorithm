santa = list('BTSKR')
n = int(input())
path = ['']*n
cnt = 0
used =[0]*len(santa)

def recur(level):
    global cnt
    if level==n:
        for t in range(len(path)):
            if path[t] == 'S':
                cnt +=1
        return

    for i in range(len(santa)):
        if used[i]==0:
            used[i]=1
            path[level]=santa[i]
            recur(level+1)
            used[i]=0

recur(0)
print(cnt)