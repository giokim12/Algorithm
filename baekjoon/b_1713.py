N = int(input())
M = int(input())
arr = list(map(int, input().split()))
bucket = [0]*101
for i in range(len(arr)):
    bucket[arr[i]] += 1

print(bucket)