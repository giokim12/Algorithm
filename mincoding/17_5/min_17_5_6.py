password = [3, 7, 4, 9]
inp = list(map(int, input().split()))

def isSame(k):
    cnt = 0
    for i in range(len(k)):
        if password[i] == k[i]:
            cnt += 1

    if cnt == 4:
        print('pass')
    else:
        print('fail')

isSame(inp)