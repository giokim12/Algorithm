N = int(input())
arr = []
for i in range(N):
    n = int(input())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)

total = 0
for i in arr:
    total +=i
print(total)