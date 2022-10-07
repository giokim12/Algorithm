T = int(input())

for tc in range(1, 1+T):
    test_case = int(input())
    arr = list(map(int, input().split()))
    bucket = [0]*101

    for i in range(len(arr)):
        bucket[arr[i]] += 1

    MAX = 0
    MAX_idx = 0
    for i in range(len(bucket)):
        if bucket[i]>=MAX:
            MAX = bucket[i]
            MAX_idx = i

    print(f'#{test_case} {MAX_idx}')