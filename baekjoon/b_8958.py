testcases = int(input())

for tc in range(testcases):
    arr = list(input())
    total = 0
    cnt = 1
    for i in range(len(arr)):
        if arr[i] =='O':
            total += cnt
            cnt +=1
        else:
            cnt = 1
            continue

    print(total)
