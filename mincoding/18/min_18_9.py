apt = [[15, 18, 17],
       [4, 6, 9],
       [10, 1, 3],
       [7, 8, 9],
       [15, 2, 6]]

family= list(map(int, input().split()))

def isPattern(list_1):
    global apt
    for i in range(5):
        if list_1 == apt[i]:
            print(f'{5-i}층')
isPattern(family)