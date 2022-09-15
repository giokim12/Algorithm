arr = [list('___'),
       list('___'),
       list('ATK'),
       list('___'),
       list('___')]

def switchseats(person, direction):
    for i in range(5):
        for j in range(3):
            if arr[i][j] == person:
                if direction == 'UP':
                    arr[i][j], arr[i - 1][j] = arr[i - 1][j], arr[i][j]
                    return
                elif direction == 'DOWN':
                    arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
                    return
                elif direction == 'RIGHT':
                    arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
                    return
                elif direction == 'LEFT':
                    arr[i][j], arr[i][j - 1] = arr[i][j - 1], arr[i][j]
                    return

for k in range(7):
    person, direction = input().split()
    switchseats(person, direction)


for i in arr:
    print(*i, sep= '')