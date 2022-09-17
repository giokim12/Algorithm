arr = list('BGTK')
n = int(input())
path=['']*5
def p(level):

    if level == n:
        for j in range(len(path)):
            print(path[j], end='')
        print()
        return

    for i in range(4):
        path[level] = arr[i]
        p(level+1)


p(0)
