a = []
for _ in range(4):
    a.append(input())

a = sorted(a, key= lambda x: len(x))

for i in range(4):
    print(a[i])