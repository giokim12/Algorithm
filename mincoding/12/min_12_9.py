arr = [['' for _ in range(3)] for _ in range(3)]
a = input()

cnt = 7
for i in range(10):
    if a == str(i):
        for m in range(3):
            for n in range(3):
                if n>=m:
                    cnt -= 1
                    arr[m][n] = cnt
                else:
                    arr[m][n] = ' '



# if a.isupper() == True:
#     for m in range(3):
#         for n in range(3):
#             if n >= m:
#                 cnt -= 1
#                 arr[m][n] = cnt
#             else:
#                 arr[m][n] = ' '
#             print(arr[m][n], end='')
#         print()

c=0
if a.isupper() == True:
    for m in range(2, -1, -1):
        for n in range(3):
            if m >= n:
                c += 1
                arr[m][n] = c
            else:
                arr[m][n] = ' '

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end='')
    print()