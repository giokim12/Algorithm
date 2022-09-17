arr = list(input())

for i in range(len(arr)):
    for j in range(i+1):
        print(arr[j], end='')
    print()
