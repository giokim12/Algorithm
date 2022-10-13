N = int(input())

group_word_cnt = 0
for tc in range(N):
    word = input()
    used = [0]*200

    flg = 0
    used[ord(word[0])] = 1
    for i in range(1, len(word)):
        if used[ord(word[i])] == 0 or word[i-1]== word[i]:
            used[ord(word[i])] +=1
        else:
            flg =1
            break

    if flg == 0:
        group_word_cnt +=1


print(group_word_cnt)