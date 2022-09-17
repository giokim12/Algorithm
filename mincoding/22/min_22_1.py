arr=['A','B','C']
path=['']*5


def abc(level):
    if level==2:
        for j in range(len(path)):
            print(path[j], end='')
        print()
        return

    for i in range(3):
        path[level]=arr[i]
        abc(level+1)

abc(0)