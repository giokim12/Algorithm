n = int(input())
change = list(map(int, input().split()))
stay = list(map(int, input().split()))

change = sorted(change, key=lambda x: x)
stay = sorted(stay, key=lambda x: -x)

total = 0
for i in range(n):
    total+= change[i]*stay[i]

print(total)