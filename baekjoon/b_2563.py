bucket = [[0]*101 for _ in range(101)]

T = int(input())

for tc in range(T):
    x, y = map(int, input().split())

    for i in range(10):
        for j in range(10):
            bucket[y+i][x+j] +=1


area = 0
for i in range(101):
    for j in range(101):
        if bucket[i][j] >0:
            area +=1

print(area)