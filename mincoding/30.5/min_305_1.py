n = int(input())

if n%360 ==0:
    print('12 9 3 6')
elif n%360 ==90:
    print('9 6 12 3')
elif n%360 ==180:
    print('6 3 9 12')
else:
    print('3 12 6 9')