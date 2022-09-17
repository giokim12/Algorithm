arr = list(input())

cnt = 0
for i in range(int(len(arr)/2)):
    if arr[i] == arr[int(len(arr)/2)+i]:
        cnt += 1

if cnt == int(len(arr)/2):
    print("동일한문장")
else:
    print("다른문장")