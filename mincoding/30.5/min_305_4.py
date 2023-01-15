a = list(map(int, input()))
b = list(map(int, input()))
c = list(map(int, input()))

la = len(a)
lb = len(b)
lc = len(c)

if la>lb and la>lc:
    for i in range(len(a)):
        print(a[i], end='')
elif lb>lc and lb>la:
    for i in range(len(b)):
        print(b[i], end='')
elif lc>lb and lc>la:
    for i in range(len(c)):
        print(c[i], end='')

if la == lb:
    for i in range(len(a)):
        if a[i]>b[i]:
            print(a[i], end = '')
        elif a[i]<b[i]:
            print(b[i], end='')
        else:
            continue
elif lb == lc:
    for i in range(len(b)):
        if b[i]>c[i]:
            print(b[i], end = '')
        elif c[i]>b[i]:
            print(c[i], end='')
        else:
            continue
else:
    for i in range(len(a)):
        if a[i]>c[i]:
            print(a[i], end = '')
        elif c[i]>a[i]:
            print(c[i], end='')
        else:
            continue