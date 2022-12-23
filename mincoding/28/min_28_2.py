'''
7
0 0 0 0 1 0 1
0 0 0 0 0 1 0
1 1 0 1 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]



for j in range(n):
    if arr[j][0] == 1:
        print(f'boss:{j}')

print(f'under:',end='')
for i in range(n):
    if arr[0][i] == 1:
        print(f'{i}',end=' ')