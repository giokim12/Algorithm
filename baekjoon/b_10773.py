N = int(input())
arr = [ int(input()) for _ in range(N)]

for i in range(N):
    if arr[i] == 0:
        for j in range(i-1, -1, -1):
            if arr[j] != 0:
                arr[j]=0
                break
total = 0
for i in range(N):
    total += arr[i]

print(total)





