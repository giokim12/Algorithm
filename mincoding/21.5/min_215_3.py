arr= list(input())
l1, l2 = map(str, input().split())

def changeHash(x):
    global arr
    dx = [-1, 1]

    for i in range(2):
        nx = x + dx[i]

        if nx<0 or nx>len(arr)-1:
            continue
        elif arr[nx]==l1 or arr[nx]==l2:
            continue
        else:
            arr[nx] = '#'


for s in range(len(arr)):
    if arr[s]== l1 or arr[s]== l2:
        changeHash(s)

for k in range(len(arr)):
    print(arr[k], end='')
