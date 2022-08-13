a = int(input())

def abc(n, cnt):
    if cnt == 3:
        print(n, end = ' ')
        return
    abc(n+2, cnt+1)
    print(n, end = ' ')


abc(a , 0)