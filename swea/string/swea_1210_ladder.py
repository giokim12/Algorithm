T = 10
for tc in range(1, T+1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 시작점 찾기 (맨끝줄의 x좌표 찾기)
    x = 0
    for s in range(100):
        if ladder[99][s] == 2:
            x= s
    y = 99

    # 다이렉트배열 (오른쪽이나 왼쪽에 갈수있는 길 있으면 오,왼 먼저인거 확인)
    dy = [0, 0, -1]
    dx = [-1, 1, 0]


    while y>=0:
        for i in range(3):
            # 다음에 가는 칸 확인
            ny = y+dy[i]
            nx = x+dx[i]
            #범위 벗어나면 다음거로 넘어가기
            if nx<0 or nx>99 or ny>99:
                continue

            if ladder[ny][nx] == 1:
                idx = i
                ladder[y][x] = 3 #이미 갔던 칸 안가도록 체크 해주기
                y+=dy[idx]
                x+=dx[idx]
                break

    print(f'#{tc} {x}')



