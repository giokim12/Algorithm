a = [3, 7, 4, 1, 9, 4, 6, 2]
ind = int(input())

def what_index(n):
    print(a[n], end = ' ')
    if n ==0:
        return
    what_index(n-1)
    print(a[n], end = ' ')

what_index(ind)