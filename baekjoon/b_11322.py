T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    K = 1

    while True:
        if K%N==0:
            print(K)
            break
        else:
            K*=10
