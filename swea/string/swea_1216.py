T = 10

for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(100)]
    MAX = 0
    cnt = 0
    #가로로 가장 큰 회문 찾기
    for i in range(100):
        for j in range(100):
            for k in range(100-j+1):
                if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                    cnt= k
                    if cnt>MAX:
                        MAX=cnt

    #세로로 가장 큰 회문 찾기
    #먼저 가로세로 바꾼 arr 새로 만들기
    temp_out = []
    for s in range(100):
        temp_in = []
        for t in range(100):
            temp_in.append(arr[t][s])
        temp_out.append(temp_in)

    for n in range(100):
        for m in range(100):
            for l in range(100-m+1):
                if temp_out[n][m:m+l] == temp_out[n][m:m+l][::-1]:
                    cnt=l
                    if cnt > MAX:
                        MAX = cnt



    print(f'#{tc} {MAX}')



