def lotto(level, start):

    if level==6:
        print(*path)
        return

    for i in range(start, n):
        path[level] = lotto_numbers[i]
        lotto(level+1, i+1)



while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    if n == 0 and len(arr) == 1:
        break
    else:
        lotto_numbers = arr[1:]
        used = [0]*6
        path = [0]*6
        lotto(0, 0)
        print()



