totalcards, pickedcards = map(int, input().split())
arr = list(map(int, input().split()))
path = [0]*pickedcards
used = [0]*totalcards
MIN = 21e8
MIN_path = []

def rcr(lvl, total):
    global MIN, MIN_path

    if lvl ==pickedcards:
        if total<MIN:
            MIN = total
            MIN_path = path
            MIN_path = sorted(path, key=lambda x: x)
        return


    for i in range(totalcards):
        if used[i]==0:
            used[i]=1
            path[lvl]=arr[i]
            rcr(lvl+1, total*arr[i])
            used[i]=0

rcr(0, 1)
print(*MIN_path)