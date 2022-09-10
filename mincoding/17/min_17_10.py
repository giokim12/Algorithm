arr = list(map(int, input().split()))

for i in range(len(arr)):
    if i%2 != 0:
        arr[i] = 0
minNum = 99999
minInd = 0
for i in range(len(arr)):
    minInd += 1
    if arr[i] <minNum and arr[i]>0:
        minNum = arr[i]

print(minNum)
print(f'arr[{}]={minNum}')