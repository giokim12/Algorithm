a = ['M', 'T', 'K', 'C']

findme = input()

def isExist(i):
    for i in range(len(a)):
        if a[i] == findme:
            return 1
        else:
            continue
    return 0


if isExist(findme)==1:
    print("발견")
else:
    print("미발견")
