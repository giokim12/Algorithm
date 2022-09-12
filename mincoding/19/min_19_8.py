arr = [list(map(int, input().split())) for _ in range(4)]

def rectSum(x, y):
    directx = [0, 1, 2, 0, 1, 2]
    directy = [0, 0, 0, 1, 1, 1]
    sum1 = 0
    for i in range(6):
        ny = y+ directy[i]
        nx = x+ directx[i]

        if ny<0 or nx<0 or ny>3 or nx>3: continue
        sum1 += arr[ny][nx]

    return sum1


MAX = 0
MAXx = 0
MAXy = 0
for s in range(4):
    for t in range(4):
        if rectSum(s, t)> MAX:
            MAX = rectSum(s, t)
            MAXy = s
            MAXx = t

print(f'({MAXx},{MAXy})')
