N, M = map( int, input().split())

answers = []
for i in range(N):
    temp = input()
    answers.append(temp)

cnt = 0
for j in range(M):
    temp2 = input()
    if temp2 in answers:
        cnt +=1

print(cnt)