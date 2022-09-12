arr = [[3, 5, 4],
       [1, 1, 2],
       [1, 3, 9]]

y, x = map(int, input().split())

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
sum = 0
for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if ny<0 or nx<0 or nx>2 or ny>2: continue

    sum += arr[ny][nx]

print(sum)