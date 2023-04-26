def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        temp = 0
        for j in range(len(photo[i])):
            for k in range(len(name)):
                if photo[i][j]== name[k]:
                    temp += yearning[k]
        answer.append(temp)
    return answer