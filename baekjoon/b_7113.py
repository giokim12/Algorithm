
import sys
sys.setrecursionlimit(10**7)
N, M = map(int, input().split())
cnt = 0

def rcr(n, m):
    global cnt
    if n==m:
        cnt +=1
        return

    if n>m:
        cnt+=1
        rcr(n-m, m)
    elif m>n:
        cnt+=1
        rcr(n, m-n)

rcr(N, M)
print(cnt)
'''

n, m = map(int, input().split())
cnt = 0

while True:
    if n>m:
        n = n-m
        cnt+=1
    elif m>n:
        m = m-n
        cnt+=1
    elif n==m:
        cnt+=1
        break

print(cnt)
'''