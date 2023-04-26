def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        compare = t[i:i+len(p)]
        print(compare)
        if int(compare)<=int(p):
            answer += 1
    return answer