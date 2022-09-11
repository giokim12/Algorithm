employees = [
    [65000, 35, 42, 70],
    [70, 35, 65000, 1300],
    [65000, 30000, 38, 42]
]

bucket = [0]*99999

for i in range(3):
    for j in range(4):
        bucket[employees[i][j]] +=1

maxAttend = 0
maxInd = 0
for i in range(len(bucket)):
    if bucket[i]>maxAttend:
        maxAttend= bucket[i]
        maxInd = i

print(maxInd)