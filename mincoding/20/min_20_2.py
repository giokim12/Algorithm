# def count_down(k):
#     print(k)
#     if k == 0:
#         return
#     count_down(k-1)
#     print(k)
#
#
# count_down(4)

n=int(input())
def count_down(k):
    print(k, end='')
    if k == 0:
        return
    count_down(k-1)
    print(k, end='')


count_down()