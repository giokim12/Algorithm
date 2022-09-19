arr = [10, 40, 60]
path = [0]*10
MIN = 21e8
n = int(input())

def rcr(level, total, cnt):
    global MIN

    if total>n:
        return
    elif total==n:
        if cnt < MIN:
            MIN = cnt
        return

    for i in range(len(arr)):
        rcr(level+1, total+arr[i], cnt+1)

rcr(0, 0, 0)
print(MIN)

