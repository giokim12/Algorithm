arr = [list(map(int, input().split())) for _ in range(4)]
MAX = -1
for i in range(4):
    for j in range(8):
        if arr[i][j] != 0:
            n = 0
            while True:
                if i+n >3:
                    break
                elif arr[i+n][j] != 0:
                    n+=1
                else:
                    break
            m = 0
            while True:
                if j+m >7:
                    break
                elif arr[i][j+m] != 0:
                    m += 1
                else:
                    break

            total = 0
            for a in range(n):
                for b in range(m):
                    if arr[i+a][j+b] ==0:
                        break
                    else:
                        total += arr[i+a][j+b]

            if total > MAX:
                MAX = total

print(MAX)