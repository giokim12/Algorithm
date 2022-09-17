n = int(input())
arr = []
for k in range(1, n+1):
    arr.append(k)
path = [0]*4

def recur(level):

    if level == 4:
        for j in range(4):
            print(path[j], end='')
        print()
        return

    for i in range(len(arr)):
        path[level] = arr[i]
        recur(level+1)




recur(0)

