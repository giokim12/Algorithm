n = int(input())

def divide_two(k):
    if k == 0:
        return
    divide_two(k//2)
    print(k, end = ' ')

divide_two(n)