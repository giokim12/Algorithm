a = list(map(int, input().split()))

for i in range(len(a)):
    if i%2 != 0:
        a[i]=0


minNum = 99999
minInd = 0
for i in range(len(a)):
    if a[i]<minNum and a[i] != 0:
        minNum = a[i]
        minInd = i

print(f'arr[{minInd}]={minNum}')