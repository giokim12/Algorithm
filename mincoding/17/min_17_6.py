arr1 = [[0, 0, 0, 1], [1, 1, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
arr2 = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]

arr3= []
for i in range(4):
    arr3.append([])
    for j in range(4):
        arr3[i].append(arr1[i][j]+arr2[i][j])
        if arr3[i][j] == 0:
            print(f'({i},{j})')