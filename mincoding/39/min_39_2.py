n = int(input())
arr = [500, 100, 50, 10]

total = 0
for i in range(4):
    if n//arr[i]>0:
        total += n//arr[i]
        n -= n//arr[i]*arr[i]
    else:
        continue

print(total)