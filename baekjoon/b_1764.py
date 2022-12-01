# N, M = map(int, input().split())
# arr = [input() for _ in range(N+M)]
#
# see = set(arr[:N])
# hear = set(arr[N+1:])
#
# see_hear = list(set(see)&set(hear))
#
# print(len(see_hear))
# see_hear.sort()
# print(''.join(see_hear), end='')

N , M = map(int,input().split())
arr_1 = set()
arr_2 = set()

for _ in range(N):
    arr_1.add(input())
for _ in range(M):
    arr_2.add(input())

arr = sorted(list(arr_1 & arr_2))
print(len(arr))

for i in arr:
    print(i)