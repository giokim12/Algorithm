# T = int(input())
#
# for tc in range( 1, T+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     arr = sorted(arr, key= lambda x: x)
#     print(f'#{tc} {arr[-1]-arr[0]}')


## sort 안쓰고 푼거

# T = int(input())
#
# for j in range(T):
#     ind_case_n = int(input())
#     a = list(map(int, input().split()))
#     result = 0
#     max_n = 0
#     min_n = 99999999999
#
#     for i in a:
#         if i > max_n:
#             max_n = i
#
#         if i < min_n:
#             min_n = i
#
#         result = max_n - min_n
#
#     print(f'#{j+1} {result}')

#min max 함수
T = int(input())

for tc in range( 1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {max(arr)-min(arr)}')
