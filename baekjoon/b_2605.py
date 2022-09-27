N = int(input())
arr = list(map(int, input().split()))
bucket = []

for i in range(N):
    bucket.insert(-arr[i], i+1)


for i in range(N):
    print(bucket[i], end=' ')