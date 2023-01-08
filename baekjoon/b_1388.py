# n, m = map(int, input().split())
# arr = [list(input()) for _ in range(n)]
# total = 0
# for i in range(n):
#     row_sum = 1
#     for j in range(1, m):
#         if arr[i][j-1] != arr[i][j]:
#             row_sum += 1
#
#
#     total += row_sum
#
# print(total)

def dfs(x, y):
    # 벽을 만나면 False 반환
    if x < -1 or x > N - 1 or y < -1 or y > M - 1:
        # print('2')
        return False

    # 현재 index가 이미 방문했던 곳이라면 False 반환
    if visited[x][y] == True:
        # print('1')
        return False

    # 현재 위치 방문 처리
    visited[x][y] = True
    # 현재 index의 모양이 '-'라면
    if graph[x][y] == '-' and (y == M - 1 or graph[x][y + 1] == '-'):
        dfs(x, y + 1)  # 오른쪽으로 이동하고
    elif graph[x][y] == '|' and (x == N - 1 or graph[x + 1][y] == '|'):
        dfs(x + 1, y)  # 아래쪽으로 이동
    return True


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

visited = []
for i in range(N):
    temp = []
    for j in range(M):
        temp.append(False)
    visited.append(temp)

count = 0
for x in range(N):
    for y in range(M):
        if dfs(x, y) == True:
            count += 1

print(count)