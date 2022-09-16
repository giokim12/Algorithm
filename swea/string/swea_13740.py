'''
1
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
'''

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]

    ans=[]
    #가로줄으로 봤을 때 회문이 있는 경우
    for j in range(n-m+1): #y축 가면서 확인
        for i in range(n): #x축 가면서 확인
            if arr[i][j:j+m] == arr[i][j:j+m][::-1]: #거꾸로 뒤집은거랑 똑같은지 (회문 맞는지)
                ans = arr[i][j:j+m]

    if ans == []:
        #세로줄으로 봤을 때 회문이 있는 경우
        t_out = []
        for s in range(n): #x축
            t_in = []
            for t in range(n): #y축
                t_in.append(arr[t][s])
            t_out.append(t_in)

        for y in range(n-m+1): #y축 가면서 확인
            for z in range(n): #x축 가면서 확인
                if t_out[z][y:y+m] == t_out[z][y:y+m][::-1]: #거꾸로 뒤집은거랑 똑같은지 (회문 맞는지)
                    ans = t_out[z][y:y+m]


    print(f'#{tc}', end = ' ')
    for q in range(len(ans)):
        print(ans[q], end='')
    print()
'''

arr = list('ABCDEFGHIJK')

print(arr[0:len(arr)])
print(arr[0:len(arr)][::-1])
print(arr[len(arr)-1:0:-1])
'''