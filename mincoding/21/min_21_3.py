# level, branch = map(int, input())
level = 2
branch = 3

def lev_br(br, cnt):

    if cnt == level:
        return

    for i in range(br):
        lev_br(br, cnt+1)

lev_br(branch, level)