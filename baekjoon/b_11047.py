N, K = map(int, input().split())
money = []
for i in range(N):
    temp = int(input())
    money.append(temp)
# print(money)
cnt = 0
while K>0:
    for i in range(N-1, -1, -1):
        if K//money[i] == 0:
            continue
        elif K//money[i] > 0:
            cnt += K//money[i]
            K = K % money[i]



print(cnt)

