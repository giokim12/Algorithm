arr = [input() for _ in range(4)]
MAX, MIN, MAX_idx, MIN_idx = 0, 99999, 0, 0

def recur(level):
    global MAX, MIN, MAX_idx, MIN_idx

    if level ==4:
        print(f'긴문장:{MAX_idx}')
        print(f'짧은문장:{MIN_idx}')
        return

    if len(arr[level])>MAX:
        MAX = len(arr[level])
        MAX_idx = level
    if len(arr[level])<MIN:
        MIN = len(arr[level])
        MIN_idx = level
    recur(level+1)

recur(0)