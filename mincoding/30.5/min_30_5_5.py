arr= list(input())
n = int(input())
path = [0]*n

def p(lv):
    if lv == n:
        for i in range(n):
            print(path[i], end='')
        print()
        return

    for i in range(len(arr)):
        path[lv] = arr[i]
        p(lv+1)



p(0)