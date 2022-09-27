MAP= [[3, 5, 4, 2, 2, 3],
    [1, 3, 3, 3, 4, 2],
    [5, 4, 4, 2, 3, 5]]

price = list('TPGKC')

y, x = map(str, input().split())
x = int(x)
y = ord(y)-ord('A')

idx = 0
for i in range(3):
    for j in range(6):
        idx = MAP[y][x-1]


print(price[idx-1])