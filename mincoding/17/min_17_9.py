vect = [[3, 7, 4], [2, 2, 4], [2, 2, 5]]
target = list(map(int, input().split()))

def CountNum(t):
    cnt = 0
    for m in range(3):
        for n in range(3):
            if t == vect[m][n]:
                cnt += 1
    return cnt

tar = []
for i in range(len(target)):
    tar.append(CountNum(target[i]))
# print(tar)
maxN = 0
maxIndex =0
for i in range(3):
    if tar[i] > maxN:
        maxN = tar[i]
        maxIndex = i
# print(maxN)
# print(maxIndex)

print(target[maxIndex])
