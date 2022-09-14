a = [3, 4, 1, 1, 2, 6, 8, 7, 8, 9, 10]
startIndex = int(input())

def getSum(k):
    cnt = -1
    s = 0
    for i in range(5):
        cnt +=1
        s += a[k+cnt]
    return s

print(getSum(startIndex))