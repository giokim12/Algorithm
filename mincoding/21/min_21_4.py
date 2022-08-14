n = int(input())

def recur(level, k):
    print(level, end= '')
    if level == k:
        return

    for i in range(2):
        recur(level + 1, k)

recur(0, n)