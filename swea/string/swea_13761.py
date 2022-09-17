T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    def findPattern(idx):
        for i in range(len(B)):
            if A[idx+i] != B[i]:
                return 0
        return 1


    cnt = 0
    for j in range(len(A)):
        if findPattern(j)==1:
            cnt+=1

    print(f'#{tc} {len(A)-cnt*(len(B)-1)}')



