abc = list(map(str, input()))


def maxIndex(k):
    cnt1 = 0
    for i in range(len(k)):
        if ord(k[i])>cnt1:
            cnt1= ord(k[i])

    for i in range(len(k)):
        if chr(cnt1) == k[i]:
            print(i)

maxIndex(abc)

def minIndex(k):
    cnt2 = 9999999
    for i in range(len(k)):
        if ord(k[i])<cnt2:
            cnt2= ord(k[i])

    for i in range(len(k)):
        if chr(cnt2) == k[i]:
            print(i)
minIndex(abc)