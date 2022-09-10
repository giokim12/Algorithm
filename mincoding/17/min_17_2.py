a = [5, 9, 4, 6, 1, 5, 8, 9]
n, m = map(int, input(). split())


for i in range(n, len(a)):
    if m == a[i]:
        print(i-n)
