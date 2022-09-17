T = int(input())

for tc in range(1, T+1):
    test_list = list(input())
    long_list = list(input())

    MAX = 0

    for i in range(len(test_list)):
        cnt = 0
        for j in range(len(long_list)):
            if test_list[i] == long_list[j]:
                cnt += 1

        if cnt>MAX:
            MAX = cnt

    print(f'#{tc} {MAX}')
