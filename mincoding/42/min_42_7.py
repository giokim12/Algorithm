buy_name = list('abcdefg')
buy_price = [15, 20, 44, 22, 55, 16, 45]
total = 0
arr = list(input())
arr1 = [0]*len(arr)
path=['']*len(buy_name)
for t in range(len(arr)):
    for s in range(len(buy_name)):
        if buy_name[s]==arr[t]:
            total+=buy_price[s]
            arr1[t]=buy_price[s]
throw_out = int(input())
MAX  = 0
used = [0]*len(arr1)

def rcr(lvl, ttl):
    global MAX
    if lvl == len(arr)-throw_out:
        if ttl%10 == 0 and ttl > MAX:
            MAX = ttl
        return


    for i in range(len(arr)):
        if used[i]==0:
            used[i]=1
            path[lvl]=arr1[i]
            rcr(lvl+1, ttl+arr1[i])
            used[i]=0

rcr(0, 0)
print(MAX)

