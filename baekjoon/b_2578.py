bingo_board = [list(map(int, input().split())) for _ in range(5)]
temp = [list(map(int, input().split())) for _ in range(5)]

numbers_called_by_MC = []
for i in range(5):
    for j in range(5):
        numbers_called_by_MC.append(temp[i][j])

# for m in range(5):
#     for n in range(5):
#         print(bingo_board[m][n], end = ' ')
#     print()
#
#
# print(numbers_called_by_MC)

#번호 불리면
#board 에서 찾아서 0으로 바꾸기
#대각선이나 한줄이 다 0이면
#빙고숫자 +=1


def find_and_change(n):
        global bingo_board
    for s in range(5):
        for t in range(5):
            if n == bingo_board[s][t]:
                bingo_board[s][t] = 0
                return

def find_bingo(bingo_board):
    bingo_cnt = 0
    #가로
    for p in range(5):
        cnt_temp = 0
        for q in range(5):
            if bingo_board[p][q]==0:
                cnt_temp +=1
        if cnt_temp ==5:
            bingo_cnt +=1
    #세로
    for a in range(5):
        cnt_temp = 0
        for b in range(5):
            if bingo_board[b][a]==0:
                cnt_temp +=1
        if cnt_temp ==5:
            bingo_cnt +=1

    #대각선
    cnt_temp = 0
    for x in range(5):
        if bingo_board[x][x]==0:
            cnt_temp += 1

    if cnt_temp == 5:
        bingo_cnt +=1

    #다른대각선
    cnt_temp = 0
    for y in range(5):
        if bingo_board[y][4-y]==0:
            cnt_temp += 1

    if cnt_temp == 5:
        bingo_cnt +=1

    return bingo_cnt



for k in range(25):
    find_and_change(numbers_called_by_MC[k])
    # print(find_bingo(bingo_board))
    if find_bingo(bingo_board) >= 3:
        print(k+1)
        break
#
# for m in range(5):
#     for n in range(5):
#         print(bingo_board[m][n], end = ' ')
#     print()

