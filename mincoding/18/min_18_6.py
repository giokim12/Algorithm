town = [
    ['C', 'D', 'A'],
    ['B', 'M', 'Z'],
    ['Q', 'P', 'O']
]

blacklist = list(map(str, input()))


def isExist(k):
    for i in range(3):
        for j in range(3):
            if k == town[i][j]:
                return True
    return False

cnt2 = 0
for i in range(4):
    if isExist(blacklist[i]) != False:
        cnt2 += 1
    # print(isExist(blacklist[i]))

print(f'{cnt2}명')


