a, b = map(str,input().split())

a1 = []
b1 = []
for i in range(2, -1, -1):
    a1.append(a[i])
    b1.append(b[i])

a2 = ''.join(a1)
b2 = ''.join(b1)

print(max(int(a2), int(b2)))