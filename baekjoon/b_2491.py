N = int(input())
arr = list(map(int, input().split()))

MAX_up = 1
cnt1 = 1
MAX_down = 1
cnt2 = 1
for i in range(1, N):
    if arr[i-1]<=arr[i]:
        cnt1 +=1
        if cnt1 > MAX_up:
            MAX_up = cnt1
    else:
        cnt1 = 1
        continue


for i in range(1, N):
    if arr[i-1]>=arr[i]:
        cnt2 +=1
        if cnt2 > MAX_down:
            MAX_down = cnt2
    else:
        cnt2 = 1
        continue

print(max(MAX_up, MAX_down))



