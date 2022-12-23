name=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
arr=[ [0, 1, 1, 0, 0, 0, 0, 1], #A
      [0, 0, 0, 0, 0, 0, 0, 0], #B
      [0, 0, 0, 1, 1, 0, 1, 0], #C
      [0, 0, 0, 0, 0, 1, 0, 0], #D
      [0, 0, 0, 0, 0, 0, 0, 0], #E
      [0, 0, 0, 0, 0, 0, 0, 0], #F
      [0, 0, 0, 0, 0, 0, 0, 0], #G
      [0, 0, 0, 0, 0, 0, 0, 0]  #H
]
find = input()
findInd = 0
for i in range(8):
    if find == name[i]:
        findInd = i
findBro = 0
for j in range(8):
      for i in range(8):
           if arr[i][j]== findInd:
                 findBro = i

flg = 0
for i in range(8):
    if arr[findBro][i] !=0 and i != findInd:
        flg = 1
        print(name[i], end=' ')

if flg == 0:
    print('없음')