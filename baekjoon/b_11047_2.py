N, K = map(int, input().split())
money = []
for i in range(N):
    temp = int(input())
    money.append(temp)
cnt = 0
while K:
    for i in range(N-1, -1, -1):
        if K//money[i] > 0:
            cnt += K//money[i]
            K = K % money[i]

print(cnt)

