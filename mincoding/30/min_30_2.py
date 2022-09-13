n = int(input())

def dfs(start_node):
    stack = [start_node]
    used = []
    nums = 0

    while stack:
        node = stack.pop()
        if node not in used:
            used.append(node)
            if len(used)>=2:
                nums += arr[used[-2]][used[-1]]
            elif len(used)<2:
                nums = 0
            for i in range(len(arr[node]) - 1, -1, -1):
                if arr[node][i] != 0:
                    stack.append(i)

            print(used[-1], nums)






arr = [[0, 0, 1, 0, 2, 0],
       [5, 0, 3, 0, 0, 0],
       [0, 0, 0, 0, 0, 7],
       [2, 0, 0, 0, 8, 0],
       [0, 0, 9, 0, 0, 0],
       [4, 0, 0, 7, 0, 0]]

dfs(n)
