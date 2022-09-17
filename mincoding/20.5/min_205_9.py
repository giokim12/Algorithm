arr = [[3, 5, 4, 2, 5],
       [3, 3, 3, 2, 1],
       [3, 2, 6, 7, 8],
       [9, 1, 1, 3, 2]]
y1, x1 = map(int, input().split())

def PatternSum(y,x):
    sum1 = 0
    for s in range(y1):
        for t in range(x1):
            sum1 += arr[y+s][x+t]
    return sum1
MAX = 0
MAXX = 0
MAXY = 0
for i in range(5-y1):
    for j in range(6-x1):
        # PatternSum(i, j)

        if MAX < PatternSum(i, j):
            MAX = PatternSum(i, j)
            MAXX = j
            MAXY = i

print(f'({MAXY},{MAXX})')
