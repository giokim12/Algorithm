arr = []
for i in range(9):
    n = int(input())
    arr.append(n)

for i in range(8):
    for j in range(i+1, 9):
        if sum(arr)-(s[i]+s[j])==100:
            fake1 = s[i]
            fake2 = s[j]

arr.remove(fake1)
arr.remove(fake2)

for i in arr:
    print(i)