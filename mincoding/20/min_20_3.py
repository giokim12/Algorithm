n = list(map(int, input().split()))


def michael(k):
    print(n[k], end=' ')
    if k== len(n)-1:
        return

    michael(k+1)
    print(n[k], end=' ')

michael(0)