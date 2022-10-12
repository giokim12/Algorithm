T = int(input())

for tc in range(1, 1+T):
    arr = list(input())

    for i in range(0, len(arr), 3):
        print(arr[i], arr[i+1], arr[i+2])
