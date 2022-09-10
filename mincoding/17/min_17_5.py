a = [[3, 5, 9], [4 ,2 ,1], [5, 1, 5]]

#입력받은 숫자 리스트
num_list = list(map(int, input().split()))

def isExist(k):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if k == a[i][j]:
                cnt += 1

    if cnt != 0:
        print(f'{k}:존재')
    else:
        print(f'{k}:미발견')


for i in range(3):
    isExist(num_list[i])