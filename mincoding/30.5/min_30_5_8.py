# 8.
heros = list('BIAH')
n = int(input())
path = [0]*len(heros)
used = [0]*n
def abc(level):
    global path
#
    if level == n:
        for i in range(level):
            print(path[i],end= ' ')
        print()
        return
#
    for i in range(len(heros)):
        if used[i] == 0:
            used[i] = 1
            path[level] = heros[i]
            abc(level+1)
            used[i] = 0
#
abc(0)
print(*path)
# 
# 8.
# heros = list('BIAH')
# N = int(input())
# idx = 0
# cnt = 0
# while True:
#     if len(heros) == 1:
#         print(*heros,end= ' ')
#         break
#     for i in range(idx,len(heros)):
#         cnt += 1
#         if cnt == N:
#             print(heros[i],end=' ')
#             heros.pop(i)
#             idx = 1
#             cnt = 0
#             break