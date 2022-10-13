N = int(input())
arr = []
for i in range(N):
    a = int(input())
    arr.append(a)

arr = sorted(arr, key=lambda x: x)
for i in range(len(arr)):
    print(arr[i])