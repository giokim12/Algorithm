T = int(input())

for tc in range(1, 1+T):
    boxes, Q = map(int, input().split())
    arr = [0]*boxes
    for i in range(Q):
        L, R = map(int, input().split())

        for j in range(boxes):
            if L-1 <= j <= R-1:
                arr[j]= i+1


    print(f'#{tc}', end=' ')
    for i in range(len(arr)):
        print(arr[i], end= ' ')
    print()
