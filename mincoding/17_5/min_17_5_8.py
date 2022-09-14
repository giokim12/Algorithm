map1 = [[3, 55, 42],
        [-5, -9, -10]]

pix = [list(map(int, input().split())) for _ in range(2)]

def findLtr(k):
    cnt = 0
    for i in range(2):
        for j in range(3):
            if k == map1[i][j]:
                cnt += 1

    if cnt >0:
        return "Y"
    else:
        return "N"


for i in range(len(pix)):
    for j in range(2):
        print(findLtr(pix[i][j]),end = ' ')
    print()