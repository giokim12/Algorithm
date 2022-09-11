cardlist = list(map(str, input()))

bucket = [0]*999

for i in range(len(cardlist)):
    bucket[ord(cardlist[i])] += 1

cnt=0
for i in range(len(bucket)):
    if bucket[i] != 0:
        cnt +=1

print(f'{cnt}개')