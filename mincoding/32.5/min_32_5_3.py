arr = [list('ABCEFG'), list('HIJKLM'), list('NOPQRS')]
bucket = [[0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]

check = list(input())

dy = [1, -1, 0, 0, 0]
dx = [0, 0, 1, -1, 0]

for c in check:
    for i in range(3):
        for j in range(6):
            if c == arr[i][j]:
                for n in range(5):
                    ny = i + dy[n]
                    nx = j + dx[n]
                    if ny < 0 or nx < 0 or ny > 2 or nx > 5:
                        continue
                    else:
                        bucket[ny][nx] += 1

for i in range(3):
    for j in range(6):
        if bucket[i][j] %2 == 0:
            print(arr[i][j], end='')
        else:
            print('#', end='')
    print()
