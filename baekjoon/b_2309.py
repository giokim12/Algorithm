arr = []
for i in range(9):
    n = int(input())
    arr.append(n)
path = [0]*7

def recur(level, start, total):
    global path

    if level==7:
        if total==100:
            path.sort()
            # path = sorted(path, key=lambda x:x)
            for i in range(7):
                print(path[i])
            quit()
        return


    for i in range(start, 9):
        path[level]=arr[i]
        recur(level+1, i+1, total+arr[i])


recur(0, 0, 0)

