levelTable = [[10, 20],
              [30, 60],
              [100, 150],
              [200, 300]]

fruitCalories = list(map(int, input().split()))
counting =[0, 0, 0, 0]
def countCal(k):
    for i in range(4):
        if k>=levelTable[i][0] and k<=levelTable[i][1]:
            counting[i] +=1

for i in range(6):
    countCal(fruitCalories[i])

for i in range(len(counting)):
    print(f'lev{i}:{counting[i]}')
# print(counting)

#
# print(f'lev{i}:{counting[i]}')






