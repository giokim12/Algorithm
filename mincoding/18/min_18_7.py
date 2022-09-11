alphabet1 = [
    ['A', 'B', 'C'],
    ['A', 'G', 'H'],
    ['H', 'I', 'J'],
    ['K', 'A', 'B'],
    ['A', 'B', 'C']
]

bucket = [0]*999

for i in range(5):
    for j in range(3):
        bucket[ord(alphabet1[i][j])] +=1


for i in range(len(bucket)):
    if bucket[i] != 0:
        print(chr(i)*bucket[i], end ='')
