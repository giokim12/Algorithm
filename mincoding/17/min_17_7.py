arr1 = [[0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1]]

arr2 = [[3, 5, 4, 1, 1],
        [3, 5, 2, 5, 6]]

n= int(input())
cnt = 0
for i in range(2):
    for j in range(5):
        if arr1[i][j] ==1 and arr2[i][j] == n:
            cnt += 1
if cnt>0:
    print(f'{n} 존재')
else: print(f'{n} 없음')