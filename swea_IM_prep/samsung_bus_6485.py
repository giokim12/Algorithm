T = int(input())

for tc in range(1, 1+T):
    bucket = [0]*5001
    N = int(input())

    for i in range(N):
        start, end = map(int, input().split())
        for j in range(5001):
            if start <= j <= end:
                bucket[j] +=1

    print(f'#{tc}', end = ' ')
    P = int(input())
    for i in range(P):
        C = int(input())
        print(bucket[C], end=' ')
    print()




