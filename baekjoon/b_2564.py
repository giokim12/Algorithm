width, height = map(int, input().split())
store_cnt = int(input())
temp = []
for i in range(store_cnt+1):
    temp.append(list(map(int, input().split())))

# for i in range(store_cnt+1):
#     if temp[i][0]==1: #북쪽이면
#         temp[i][0] = 0
#     elif temp[i][0]==2: #남쪽이면
#         temp[i][0] =height
#     elif temp[i][0]==3: #서쪽이면
#         temp[i][0]= temp[i][1]
#         temp[i][1] = 0
#     elif temp[i][0]==4:
#         temp[i][0] = temp[i][1]
#         temp[i][1] = width

# print(temp)
dong0 = temp[store_cnt+1][0]
dong1 = temp[store_cnt+1][1]

total = 0
for i in range(store_cnt):
    if temp[i][0]== dong0:
        total += abs(dong1-temp[i][1])
        





