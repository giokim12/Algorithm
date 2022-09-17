arr = [input() for _ in range(5)]
floor = 1

def recur(k):
    global floor

    if k==5:
        if floor <0:
            print(f'B{-floor+1}')
        else:
            print(floor)
        return

    if arr[k]=='up':
        floor +=1
    elif arr[k]=='down':
        floor -=1

    recur(k+1)
recur(0)