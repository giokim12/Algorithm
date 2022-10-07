s_money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())

for tc in range(1, 1+T):
    total = int(input())
    idx = 0
    bucket = [0]*8

    while idx<8:
        total-=s_money[idx]

        if total<0:
            # print(total)
            total += s_money[idx]
            idx +=1
            # print(total)
            continue
        elif total == 0:
            bucket[idx] +=1
            break
        else:
            bucket[idx] +=1
            continue

    print(f'#{tc}')
    for i in range(8):
        print(bucket[i], end= ' ')
    print()
