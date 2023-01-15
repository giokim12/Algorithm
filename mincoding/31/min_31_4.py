arr = [list(input()) for _ in range(5)]

for i in range(5):
    for j in range(5):
        arr[i][1], arr[i][3] = arr[i][3],arr[i][1]
mapom = list('MAPOM')


def findMapom(a, k):
    for i in range(5):
        if a[i] == mapom:
            return 'yes'
        else:
            continue
    return 'no'



print(findMapom(arr, 5))
