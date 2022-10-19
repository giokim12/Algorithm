'''
한 정수를 만드는 조합이...
순열 (중복X)
한 정수를 만들 수 있는 조합이 여러가지
-- 나열했는데 중복되면 없애야됨
'''

n = int(input())
k = int(input())
arr = []
for _ in range(n):
    number = int(input())
    arr.append(number)
# print(arr)
path = [0]*(k+1)
used = [0]*len(arr)
check = []
def rcr(level):

    if level == k:
        word = ''
        for i in path:
            word +=str(i)

        if word not in check:
            check.append(word)

        return

    for i in range(len(arr)):
        if used[i] ==0:
            used[i] = 1
            path[level] = arr[i]
            rcr(level+1)
            used[i] = 0

rcr(0)

print(len(check))