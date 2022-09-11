abc = list(map(str, input()))
bucket = [0]*128

for i in range(len(abc)):
    bucket[ord(abc[i])] += 1

maxNum = 0
maxInd = 0
for i in range(len(bucket)):
    if bucket[i]>maxNum:
        maxNum = bucket[i]
        maxInd = i

print(chr(maxInd))
