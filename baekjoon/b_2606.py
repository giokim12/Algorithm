point = int(input())
lines = int(input())
arr = [list(map(int, input().split()))]
used = [0]*(point+1)

def rcr(a):
    used[a] = 1

    for i in range(lines):
        if arr[i][0] == a and used[arr[i][1]]==0:
            used[arr[i][1]] = 1
            rcr(arr[i][1])


rcr(1)