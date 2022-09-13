inp = int(input())

def dfs(start_node):
    stack = [start_node]
    used = []

    while stack: #스택이 비기 전까지
        node = stack.pop() #하나씩 빼기
        if node not in used: #만약에 노드가 출력에 없으면
            used.append(node) #노드를 used로 옮기기
            for i in range(len(arr[node])-1, -1, -1):
                if arr[node][i] == 1: #가로로 돌면서 값이 1 인거
                    stack.append(i) #stack에 새로 넣어주기
    # print(used)

    for i in range(len(used)):
        print(used[i], end=' ')


arr = [[0, 0, 1, 1, 0, 1],
       [0, 0, 0, 1, 1, 1],
       [0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0]]


dfs(inp)