a = [['A', 'T', 'K', "B"], ['C', 'Z', 'F', 'D'], ['H', 'G', 'E', 'I']]

m, n, q = map(str, input().split())
n1 = int(n)
q1 = int(q)

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == m:
            print(a[i+n1][j+q1])
