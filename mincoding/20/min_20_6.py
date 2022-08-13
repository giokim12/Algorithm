a, b = map(int, input().split())

def ab_rec(n, m):
    print(n, end=' ')
    if n == m:
        return
    ab_rec(n+1, m)
    print(n, end = ' ')

ab_rec(a,b)
