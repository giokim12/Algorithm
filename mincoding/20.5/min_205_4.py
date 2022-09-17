arr1 = [list(map(int, input().split())) for _ in range(4)]
bl = input()
arr2 = [list(map(int, input().split())) for _ in range(4)]
bucket = [[0]*4 for _ in range(4)]

flg = 0
for i in range(4):
    for j in range(4):
        bucket[i][j] += arr1[i][j]
        bucket[i][j] += arr2[i][j]

        if bucket[i][j] ==2:
            flg += 1
            break
        else:
            continue

if flg ==0:
    print("걸리지않는다")
else:
    print("걸리다")