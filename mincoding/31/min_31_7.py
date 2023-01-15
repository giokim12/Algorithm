n = int(input())
a=[]
for t in range(1, n+1):
    tc = input()
    a.append(tc)

def compare(k):
    if k == len(a[i]):
        return

    if ord(a[i][k]) > ord(a[j][k]):
        a[i], a[j] = a[j], a[i]
    elif ord(a[i][k]) == ord(a[j][k]):
        compare(k+1)

for i in range(len(a)-1):
    for j in range(i, len(a)):
        if len(a[i])> len(a[j]):
            a[i], a[j] = a[j], a[i]
        elif len(a[i]) == len(a[j]):
            for k in range(len(a[i])):
                compare(k)




for m in range(len(a)):
    print(a[m])

