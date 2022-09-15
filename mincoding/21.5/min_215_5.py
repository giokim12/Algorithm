vect = list(map(int, input().split()))
bucket = [0]*10

for i in range(len(vect)):
    bucket[vect[i]] += 1


for s in range(len(bucket)):
    for t in range(bucket[s]):
        print(s, end= ' ')


