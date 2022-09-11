a = [list(map(int, input().split())) for _ in range(3)]
bucket = [0]*10


for i in range(3):
    for j in range(3):
        bucket[a[i][j]] += 1

for i in range(10):
    if i != 0 and bucket[i] == 0:
        print(i, end =' ')
