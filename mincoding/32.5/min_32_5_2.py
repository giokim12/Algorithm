arr = list(input())

while True:
    cnt = 0
    for i in range(len(arr)):
        print(arr[i], end='')
        if arr[i] == '_':
            cnt += 1
        elif ord(arr[i])-ord('A') <=0:
            arr[i] = '_'
        else:
            arr[i] = chr(ord(arr[i])-1)
    print()



    if cnt == len(arr):
        break




