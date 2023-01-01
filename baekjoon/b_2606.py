'''
3
2
2 3
1 2
'''


point = int(input())
lines = int(input())
arr = [list(map(int, input().split())) for _ in range(lines)]

for i in range(lines):
    if arr[i][0]>arr[i][1]:
        arr[i][0],arr[i][1] = arr[i][1],arr[i][0]
arr = sorted(arr, key=lambda x: x[0])

used = [0]*(point+1)
cnt =0
def rcr(a):
    global cnt

    used[a] = 1


    for i in range(lines):
        if arr[i][0] == a and used[arr[i][1]]==0:
            used[arr[i][1]] = 1
            cnt+=1
            rcr(arr[i][1])


rcr(1)
print(cnt)
