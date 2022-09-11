train = [3, 7, 6, 4, 2, 9, 1, 7]
team = list(map(int, input().split()))

bucket = [0]*10

for i in range(len(team)):
    for j in range(len(train)):
        if team[i] == train[j]:
            bucket[j] += 1
# print(bucket)

for i in range(2, len(bucket)):
    if bucket[i-2] ==1 and bucket[i-1] == 1 and bucket[i] == 1:
        print(f'{i-2}번~{i}번 칸')

