name = list(map(str,input()))

def abc(n, cnt):
    print(name[n], end ='')
    if cnt ==5:
        print()
        print(name[n], end ='')
        return
    abc(n+1, cnt+1)
    print(name[n], end ='')

abc(0, 1)

