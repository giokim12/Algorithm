# n = int(input())
# graph = []
# num = []
#
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
#
# def DFS(x, y):
#     if x < 0 or x >= n or y < 0 or y >= n:
#         return False
#
#     if graph[x][y] == 1:
#         global count
#         count += 1
#         graph[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             DFS(nx, ny)
#         return True
#     return False
#
#
# count = 0
# result = 0
#
# for i in range(n):
#     for j in range(n):
#         if DFS(i, j) == True:
#             num.append(count)
#             result += 1
#             count = 0
#
# num.sort()
# print(result)
# for i in range(len(num)):
#     print(num[i])
'''

7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
'''
답
3
7
8
9
'''

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
num = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if arr[x][y] == 1:
        global count
        count += 1
        arr[x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True


count = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])