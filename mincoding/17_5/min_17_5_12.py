letter = input()
abc = []
cnt = -1
for i in range(5):
    abc.append([])
    for j in range(5):
        cnt += 1
        abc[i].append(chr(ord('A') + cnt))

for i in range(5):
    for j in range(5):
        if letter == abc[i][j]:
            print(f'{i-2},{j-2}')