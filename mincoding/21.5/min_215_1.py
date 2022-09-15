arr = [list(input()) for _ in range(4)]


ax = 0
ay = 0
bx = 0
by = 0
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            ay = i
            ax = j
        elif arr[i][j]=='B':
            by = i
            bx = j

print(abs(ax-bx)+abs(ay-by))