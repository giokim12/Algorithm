arr = list(input())
n = len(arr)

for i in range(n):
    for j in range(n-i-1, n):
        print(arr[j], end ='')
    print()
