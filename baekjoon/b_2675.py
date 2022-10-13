TC = int(input())

for tc in range(TC):
    n, word = map(str, input().split())
    n = int(n)

    for i in word:
        print(n*i, end='')
