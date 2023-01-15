P = int(input())
N = int(input())


for _ in range(N):
    #곱하기
    P = P *2
    P = str(P)
    #숫자 뒤집기
    a = []
    for i in range(len(P)):
        a.append(P[i])
    for i in range(int(len(a)/2)):
        a[i], a[len(a)-i-1] = a[len(a)-i-1],a[i]
    a_s = ''
    for i in range(len(a)):
        a_s += a[i]
    P = int(a_s)

print(P)