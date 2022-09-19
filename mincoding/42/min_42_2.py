arr = list(map(int, input().split()))
#순열 (중복X)
path = ['']*5
used = [0]*5
MAX = (-21e8)
MIN = (21e8)
value = 0

def recur(level):
    global value, MIN, MAX
    if level==5:
        value = (path[0]*path[1])-(path[2]*path[3])+path[4]
        if value>MAX:
            MAX=value
        if value<MIN:
            MIN=value
        return


    for i in range(5):
        if used[i]==0:
            used[i]=1
            path[level]=arr[i]
            recur(level+1)
            used[i]=0

recur(0)
print(MAX)
print(MIN)