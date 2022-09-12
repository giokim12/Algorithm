arr = [
    [3, 3, 5, 3, 1],
    [2, 2, 4, 2, 6],
    [4, 9, 2, 3, 4],
    [1, 1, 1, 1, 1],
    [3, 3, 5, 9, 2]
]

def sum1(y, x):
    sum2 = 0
    directy = [-1, 1, -1, 1]
    directx = [1, 1, -1, -1]

    for i in range(4):
        ny = y+directy[i]
        nx = x+directx[i]

        if ny<0 or nx<0 or nx>4 or ny>4: continue
        sum2 += arr[ny][nx]

    return sum2

MAX = 0
MAXx = 0
MAXy = 0
for s in range(5):
    for t in range(5):
        if sum1(s, t)> MAX:
            MAX = sum1(s, t)
            MAXy = s
            MAXx = t

print(MAXy, MAXx)
