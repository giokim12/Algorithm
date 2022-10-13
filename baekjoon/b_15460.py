'''
N = int(input())
scores = list(map(int, input().split()))

MAX = 0
MAX_eat = 0
for i in range(1, N-1): #betty가 먹은 숙제
    graded_scores = []
    for j in range(i, N): #내가 채점받을 숙제
        graded_scores.append(scores[j])
    #제일 낮은 성적 빼기
    lowest_grade = min(graded_scores)
    graded_scores.remove(lowest_grade)
    #나머지 평균내기
    AVER = sum(graded_scores)/len(graded_scores)
    #나머지 평균에서 제일 높은거
    if AVER>MAX:
        MAX = AVER
        MAX_eat = i

print(MAX_eat)
'''
'''
N = int(input())
scores = list(map(int, input().split()))

MAX = 0
MAX_eat = 0
SUM = sum(scores)
lowest_grade = min(scores)
for i in range(1, N-1): #betty가 먹은 숙제
    graded_scores = scores[i:]
    ate_grade = scores[i-1]
    SUM -= ate_grade
    if ate_grade == lowest_grade:
        lowest_grade = min(graded_scores)
        graded_scores.remove(lowest_grade)
    else:
        graded_scores.remove(lowest_grade)
    #나머지 평균내기
    AVER = SUM/len(graded_scores)
    #나머지 평균에서 제일 높은거
    if AVER>MAX:
        MAX = AVER
        MAX_eat = i

print(MAX_eat)
'''

N = int(input())
scores = list(map(int, input().split()))

MAX = 0
MAX_eat = 0
SUM = sum(scores[N-2:])
min_score = min(scores[N-2:])
print(SUM)
print(min_score)
for i in range(N-3, 0, -1):
    # print(scores[i])






