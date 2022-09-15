arr = [[3, 4, 1, 5],
       [3, 4, 1, 3],
       [5, 2, 3, 6]]

sum1 = [0, 0, 0, 0]
n = int(input())

for i in range(len(sum1)):
    sum1[i] = arr[0][i]+arr[1][i]+arr[2][i]

print(sum1[n])