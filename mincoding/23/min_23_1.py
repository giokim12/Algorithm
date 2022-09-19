people = list(input())
path = ['']*3
used = [0]*len(people)


def recur(level):

    if level==3:
        for j in range(len(path)):
            print(path[j], end='')
        print()
        return


    for i in range(len(people)):
        if used[i] == 0:
            used[i] = 1
            path[level] = people[i]
            recur(level+1)
            used[i] = 0

recur(0)

