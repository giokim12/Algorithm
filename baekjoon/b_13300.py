student_total, room_total = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(student_total)]
bucket = [[0]*7 for _ in range(2)]


for i in range(len(students)):
    bucket[students[i][0]][students[i][1]] += 1

# print(bucket)
room_number = 0
for i in range(2):
    for j in range(7):
        if bucket[i][j] ==0:
            continue
        elif 0<bucket[i][j]<room_total:
            room_number +=1
        elif bucket[i][j]%room_total==0:
            room_number += bucket[i][j]/room_total
        elif bucket[i][j]%room_total!=0:
            room_number += (bucket[i][j]//room_total)+1


print(int(room_number))



