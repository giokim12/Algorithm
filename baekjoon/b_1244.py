switch_number = int(input())
switches = list(map(int, input().split()))
switches.insert(0, 0)
student_number = int(input())
student_trial = [list(map(int, input().split())) for _ in range(student_number)]

def switch_light(k):
    global switches
    if switches[k]==0:
        switches[k]=1
    elif switches[k]==1:
        switches[k]=0


for i in range(student_number):
    if student_trial[i][0]==1: #남자라면
        for j in range(len(switches)):
            if j%student_trial[i][1]==0: #j가 주어진 값으로 나눠진다면
                switch_light(j) # 스위치 바꾸기
                continue #다음으로 바꿀 스위치 또 찾기
            else: continue

    elif student_trial[i][0]==2: #여자라면
        for j in range(switch_number//2):
            if student_trial[i][1]+j>switch_number or student_trial[i][1]-j<1: break
            if j==0:
                switch_light(student_trial[i][1])
                continue
            elif switches[student_trial[i][1]-j] == switches[student_trial[i][1]+j]:
                switch_light(student_trial[i][1]-j)
                switch_light(student_trial[i][1]+j)
                continue
            else: break

for i in range(1, len(switches)):
    print(switches[i], end= ' ')
    if i % 20 == 0 :
        print()

