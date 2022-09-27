n = int(input())
options = ['x', 'o']
path = ['']*n

def rcr(level):

    if level==n:
        for i in range(n):
            print(path[i], end='')
        print()
        return

    for i in range(2):
        path[level]=options[i]
        rcr(level+1)

rcr(0)