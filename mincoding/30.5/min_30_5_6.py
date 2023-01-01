n = int(input())

arr = [input() for _ in range(n)]


def checkPassword(k):
    times = 1
    for i in range(4):
        times += (ord(k[i])-65)*26**(3-i)
    print(times)


for i in range(n):
    checkPassword(arr[i])