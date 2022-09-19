arr = list(input())
path = ['']*3

def recur(level, start):

    if level==3:
        for j in range(3):
            print(path[j], end='')
        print()
        return

    for i in range(start, len(arr)):
        path[level]=arr[i]
        recur(level+1, i)

recur(0, 0)