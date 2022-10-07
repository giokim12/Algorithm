T = int(input())

for tc in range(1, 1+T):
    students = int(input())
    arr = [list(map(int, input().split())) for _ in range(students)]

    for i in range(students):
        if arr[i][0] > arr[i][1]:
            arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
    bucket = [0]*401

    for i in range(students):
        for j in range((len(bucket)+1)//2):
            if (arr[i][0]+1)//2<= j <=(arr[i][1]+1)//2:
                bucket[j] += 1
    # print(bucket)
    MAX = 0
    for i in range(len(bucket)):
        if bucket[i]>MAX:
            MAX = bucket[i]

    print(f'#{tc} {MAX}')
