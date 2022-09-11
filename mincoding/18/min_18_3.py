l1 = [[1, 3, 3, 5, 1],
      [3, 6, 2, 4, 2],
      [1, 9, 2, 6, 5]]

N1 = int(input())
bucket = [0]*99

for i in range(3):
    for j in range(5):
        bucket[l1[i][j]] += 1


for i in range(10):
    if bucket[i] == N1:
        print(i, end = ' ')
