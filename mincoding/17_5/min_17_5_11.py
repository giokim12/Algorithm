a = [3, 5, 4, 2]
mask = list(map(int, input().split()))

for i in range(4):
    if mask[i]==0:
        a[i] = 0
addNum = 0
for i in range(4):
    addNum += a[i]
print(addNum)

